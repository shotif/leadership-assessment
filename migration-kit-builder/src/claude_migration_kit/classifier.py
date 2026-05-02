"""Phase 1.5 classifier — assign each conversation to a project (or 'standalone')
using Claude Opus 4.7 via the Anthropic API.

Design notes
- One stable system prompt per run (project catalog) + a per-batch user payload
  (10 conversations at a time).
- Structured outputs (`output_config.format`) guarantee parseable JSON.
- Per-conversation payload is intentionally lean: title + first/last turns +
  3 evenly-sampled mid user turns, all truncated.
- Cost is estimated up front from token counts in the request itself.

Pricing (Opus 4.7, USD per million tokens, 2026-04 cache):
  input        = $5.00
  output       = $25.00
  cache write  = input × 1.25 = $6.25
  cache read   = input × 0.10 = $0.50
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Iterable

import anthropic

from .models import Conversation, Project

MODEL = "claude-opus-4-7"
BATCH_SIZE = 10
MAX_TOKENS = 4096

INPUT_PRICE_PER_M = 5.00
OUTPUT_PRICE_PER_M = 25.00
CACHE_WRITE_PRICE_PER_M = INPUT_PRICE_PER_M * 1.25
CACHE_READ_PRICE_PER_M = INPUT_PRICE_PER_M * 0.10

STANDALONE_SLUG = "standalone"

OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "classifications": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "conversation_id": {"type": "string"},
                    "project_slug": {"type": "string"},
                    "confidence": {"type": "number"},
                    "reason": {"type": "string"},
                },
                "required": ["conversation_id", "project_slug", "confidence", "reason"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["classifications"],
    "additionalProperties": False,
}


@dataclass
class Mapping:
    conversation_id: str
    title: str
    project_slug: str
    confidence: float
    reason: str
    needs_review: bool = False


@dataclass
class UsageTotals:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_input_tokens: int = 0
    cache_read_input_tokens: int = 0

    def add(self, usage: Any) -> None:
        self.input_tokens += getattr(usage, "input_tokens", 0) or 0
        self.output_tokens += getattr(usage, "output_tokens", 0) or 0
        self.cache_creation_input_tokens += (
            getattr(usage, "cache_creation_input_tokens", 0) or 0
        )
        self.cache_read_input_tokens += (
            getattr(usage, "cache_read_input_tokens", 0) or 0
        )

    def cost_usd(self) -> float:
        return (
            self.input_tokens / 1_000_000 * INPUT_PRICE_PER_M
            + self.output_tokens / 1_000_000 * OUTPUT_PRICE_PER_M
            + self.cache_creation_input_tokens / 1_000_000 * CACHE_WRITE_PRICE_PER_M
            + self.cache_read_input_tokens / 1_000_000 * CACHE_READ_PRICE_PER_M
        )


@dataclass
class ProjectCatalogEntry:
    slug: str
    uuid: str
    name: str
    description: str
    instructions_excerpt: str
    knowledge_filenames: list[str] = field(default_factory=list)


def truncate(s: str, n: int) -> str:
    s = (s or "").strip()
    if len(s) <= n:
        return s
    return s[: n - 1].rstrip() + "…"


def build_catalog(
    projects: list[Project], slugs_by_uuid: dict[str, str]
) -> list[ProjectCatalogEntry]:
    out: list[ProjectCatalogEntry] = []
    for p in projects:
        out.append(
            ProjectCatalogEntry(
                slug=slugs_by_uuid[p.uuid],
                uuid=p.uuid,
                name=p.name or "(untitled)",
                description=truncate(p.description or "", 240),
                instructions_excerpt=truncate(p.prompt_template or "", 600),
                knowledge_filenames=[d.name for d in p.docs[:8]],
            )
        )
    return out


def render_system_prompt(catalog: list[ProjectCatalogEntry]) -> str:
    lines = [
        "You classify past Claude conversations against a fixed list of projects "
        "from a single user's account. The user's project ↔ conversation links "
        "were lost in the data export and you are reconstructing them.",
        "",
        "For each conversation, return the single most-likely project_slug, a "
        "confidence (0.0–1.0), and a one-sentence reason. Use 'standalone' when "
        "no project is a reasonable match — vague topical similarity is not "
        "enough; ground project assignments in concrete signal (terminology, "
        "named entities, file references, instructions overlap).",
        "",
        "Available projects:",
    ]
    for entry in catalog:
        lines.append(f"\n- slug: {entry.slug}")
        lines.append(f"  name: {entry.name}")
        if entry.description:
            lines.append(f"  description: {entry.description}")
        if entry.instructions_excerpt:
            lines.append(f"  custom instructions: {entry.instructions_excerpt}")
        if entry.knowledge_filenames:
            lines.append(
                f"  knowledge files: {', '.join(entry.knowledge_filenames)}"
            )
    lines.append(f"\n- slug: {STANDALONE_SLUG}")
    lines.append("  meaning: no clear fit with any project above")
    lines.append(
        "\nReturn JSON matching the requested schema. One entry per "
        "conversation. Do not invent project_slugs — use only the slugs above."
    )
    return "\n".join(lines)


def sample_user_turns(conv: Conversation, n: int) -> list[str]:
    user_msgs = [
        m.plain_text() for m in conv.chat_messages if (m.sender or "").lower() == "human"
    ]
    if len(user_msgs) <= 2:
        return []
    middle = user_msgs[1:-1]
    if len(middle) <= n:
        return middle
    step = len(middle) / n
    return [middle[int(i * step)] for i in range(n)]


def build_payload(conv: Conversation) -> dict[str, Any]:
    msgs = conv.chat_messages
    first_user = next(
        (m.plain_text() for m in msgs if (m.sender or "").lower() == "human"), ""
    )
    last_assistant = next(
        (
            m.plain_text()
            for m in reversed(msgs)
            if (m.sender or "").lower() == "assistant"
        ),
        "",
    )
    mid = sample_user_turns(conv, 4)
    return {
        "conversation_id": conv.uuid,
        "title": conv.name or "(untitled)",
        "first_user_turn": truncate(first_user, 500),
        "last_assistant_turn": truncate(last_assistant, 500),
        "mid_user_turns": [truncate(t, 200) for t in mid],
        "message_count": len(msgs),
    }


def render_user_message(payloads: list[dict[str, Any]]) -> str:
    return (
        "Classify the following conversations. Return one entry per "
        "conversation_id, in the same order.\n\n"
        + json.dumps(payloads, ensure_ascii=False, indent=2)
    )


def chunked(seq: list[Any], n: int) -> Iterable[list[Any]]:
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


def parse_classifications(
    raw_text: str, expected_ids: list[str]
) -> list[dict[str, Any]]:
    """Defensive parse: prefer schema-validated JSON, fall back to regex."""
    try:
        obj = json.loads(raw_text)
        results = obj.get("classifications", [])
        if isinstance(results, list):
            return [r for r in results if isinstance(r, dict)]
    except json.JSONDecodeError:
        pass
    match = re.search(r"\[\s*\{.*\}\s*\]", raw_text, re.DOTALL)
    if match:
        try:
            arr = json.loads(match.group(0))
            return [r for r in arr if isinstance(r, dict)]
        except json.JSONDecodeError:
            pass
    return []


def classify_batch(
    client: anthropic.Anthropic,
    system_prompt: str,
    payloads: list[dict[str, Any]],
    valid_slugs: set[str],
) -> tuple[list[Mapping], Any]:
    user_msg = render_user_message(payloads)
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[
            {
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_msg}],
        output_config={"format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
    )
    text = next((b.text for b in response.content if b.type == "text"), "")
    expected_ids = [p["conversation_id"] for p in payloads]
    parsed = parse_classifications(text, expected_ids)

    by_id: dict[str, dict[str, Any]] = {}
    for r in parsed:
        cid = r.get("conversation_id")
        if isinstance(cid, str):
            by_id[cid] = r

    mappings: list[Mapping] = []
    for payload in payloads:
        cid = payload["conversation_id"]
        r = by_id.get(cid)
        if r is None:
            mappings.append(
                Mapping(
                    conversation_id=cid,
                    title=payload["title"],
                    project_slug=STANDALONE_SLUG,
                    confidence=0.0,
                    reason="model returned no entry for this conversation",
                )
            )
            continue
        slug = str(r.get("project_slug") or STANDALONE_SLUG)
        if slug not in valid_slugs:
            slug = STANDALONE_SLUG
        try:
            confidence = float(r.get("confidence", 0.0))
        except (TypeError, ValueError):
            confidence = 0.0
        confidence = max(0.0, min(1.0, confidence))
        mappings.append(
            Mapping(
                conversation_id=cid,
                title=payload["title"],
                project_slug=slug,
                confidence=confidence,
                reason=str(r.get("reason") or ""),
            )
        )
    return mappings, response.usage


def estimate_full_run(
    client: anthropic.Anthropic,
    system_prompt: str,
    all_payloads: list[dict[str, Any]],
) -> tuple[int, int, float]:
    """Estimate input+output tokens for the full run, without making 8 calls.

    Strategy: count tokens for the system prompt once and one representative
    batch via `messages.count_tokens`, then multiply.
    """
    sample_batch = all_payloads[:BATCH_SIZE] or all_payloads
    sample_user_msg = render_user_message(sample_batch)
    count = client.messages.count_tokens(
        model=MODEL,
        system=[{"type": "text", "text": system_prompt}],
        messages=[{"role": "user", "content": sample_user_msg}],
    )
    per_batch_input = count.input_tokens
    n_batches = (len(all_payloads) + BATCH_SIZE - 1) // BATCH_SIZE
    # Output is bounded by ~80 tokens per conversation (id + slug + confidence
    # + short reason in JSON). Round up.
    est_output_per_conv = 90
    total_input = per_batch_input * n_batches
    total_output = est_output_per_conv * len(all_payloads)
    cost = (
        total_input / 1_000_000 * INPUT_PRICE_PER_M
        + total_output / 1_000_000 * OUTPUT_PRICE_PER_M
    )
    return total_input, total_output, cost
