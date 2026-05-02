"""Phase 2 selection — filter the inventory + mappings into a kept set."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from .models import ConversationSummary, Inventory


@dataclass
class Selection:
    min_messages: int = 4
    date_floor: str = ""  # ISO date "YYYY-MM-DD" or empty
    exclude_keywords: list[str] = field(default_factory=list)
    include_projects: list[str] = field(default_factory=list)
    exclude_projects: list[str] = field(default_factory=list)
    include_conversations: list[str] = field(default_factory=list)
    exclude_conversations: list[str] = field(default_factory=list)

    @classmethod
    def from_toml(cls, path: Path) -> "Selection":
        doc = tomllib.loads(path.read_text(encoding="utf-8"))
        f = doc.get("filters", {})
        p = doc.get("projects", {})
        c = doc.get("conversations", {})
        return cls(
            min_messages=int(f.get("min_messages", 4)),
            date_floor=str(f.get("date_floor", "") or ""),
            exclude_keywords=list(f.get("exclude_keywords", [])),
            include_projects=list(p.get("include", [])),
            exclude_projects=list(p.get("exclude", [])),
            include_conversations=list(c.get("include", [])),
            exclude_conversations=list(c.get("exclude", [])),
        )

    def date_floor_parsed(self) -> date | None:
        if not self.date_floor:
            return None
        return date.fromisoformat(self.date_floor)


@dataclass
class SelectionResult:
    kept: list[ConversationSummary]
    dropped: list[tuple[ConversationSummary, str]]  # (conv, reason)


@dataclass
class ConversationView:
    """A conversation enriched with its mapped project_slug."""

    summary: ConversationSummary
    project_slug: str  # may be 'standalone'


def build_views(
    inv: Inventory, mappings_doc: dict[str, Any]
) -> list[ConversationView]:
    """Combine the inventory's conversation summaries with mappings.toml."""
    summaries: dict[str, ConversationSummary] = {}
    for p in inv.projects:
        for c in p.conversations:
            summaries[c.uuid] = c
    for c in inv.standalone_conversations:
        summaries[c.uuid] = c

    convs_doc = mappings_doc.get("conversations", {})
    out: list[ConversationView] = []
    for cid, summary in summaries.items():
        slug = (
            convs_doc.get(cid, {}).get("project_slug", "standalone")
            if isinstance(convs_doc.get(cid), dict)
            else "standalone"
        )
        out.append(ConversationView(summary=summary, project_slug=slug))
    return out


def apply(views: list[ConversationView], sel: Selection) -> SelectionResult:
    """Apply selection rules. Priority (high → low):
    1. conversations.exclude (force drop)
    2. conversations.include (force keep)
    3. projects.exclude
    4. projects.include (when non-empty)
    5. min_messages
    6. date_floor
    7. exclude_keywords (case-insensitive substring on title)
    """
    excl_convs = set(sel.exclude_conversations)
    incl_convs = set(sel.include_conversations)
    excl_projects = set(sel.exclude_projects)
    incl_projects = set(sel.include_projects)
    keywords = [k.lower() for k in sel.exclude_keywords if k]
    floor = sel.date_floor_parsed()

    kept: list[ConversationSummary] = []
    dropped: list[tuple[ConversationSummary, str]] = []

    for v in views:
        cid = v.summary.uuid
        if cid in excl_convs:
            dropped.append((v.summary, "force-excluded by conversation id"))
            continue
        if cid in incl_convs:
            kept.append(v.summary)
            continue
        if v.project_slug in excl_projects:
            dropped.append((v.summary, f"project '{v.project_slug}' excluded"))
            continue
        if incl_projects and v.project_slug not in incl_projects:
            dropped.append(
                (v.summary, f"project '{v.project_slug}' not in include list")
            )
            continue
        if v.summary.message_count < sel.min_messages:
            dropped.append(
                (
                    v.summary,
                    f"message_count {v.summary.message_count} < min {sel.min_messages}",
                )
            )
            continue
        if floor is not None and v.summary.last_message_at is not None:
            last = v.summary.last_message_at
            last_date = (
                last.astimezone(timezone.utc).date() if last.tzinfo else last.date()
            )
            if last_date < floor:
                dropped.append(
                    (
                        v.summary,
                        f"last message {last_date.isoformat()} < floor {floor.isoformat()}",
                    )
                )
                continue
        title_lower = v.summary.title.lower()
        matched_kw = next((k for k in keywords if k in title_lower), None)
        if matched_kw:
            dropped.append((v.summary, f"title matched keyword '{matched_kw}'"))
            continue
        kept.append(v.summary)

    return SelectionResult(kept=kept, dropped=dropped)


SELECTION_TEMPLATE = """\
# selection.toml — edit, then re-run with `--apply-selection` to preview the result.
#
# Rule priority (high → low):
#   1. conversations.exclude  — force drop
#   2. conversations.include  — force keep (overrides everything below)
#   3. projects.exclude       — drop the whole project
#   4. projects.include       — when non-empty, drop everything not in the list
#   5. filters.min_messages
#   6. filters.date_floor
#   7. filters.exclude_keywords (case-insensitive substring on title)

[meta]
generated_at = "{generated_at}"
inventory    = "inventory.json"
mappings     = "mappings.toml"

[filters]
# Drop conversations with fewer than this many messages.
# Default 4 trims one-off questions but keeps any real exchange.
min_messages     = {min_messages}

# Drop conversations whose last message predates this date (ISO 8601, e.g. "2025-01-01").
# Empty string disables the floor.
date_floor       = "{date_floor}"

# Drop if any of these substrings appears in the title (case-insensitive).
exclude_keywords = []

[projects]
# Slugs to include. Empty list = include all (subject to filters).
# Available slugs: {available_slugs}
include = []
# Slugs to exclude entirely.
exclude = []

[conversations]
# Force-include specific conversation UUIDs (skips all filters).
include = []
# Force-exclude specific conversation UUIDs (highest priority).
exclude = []
"""


def render_default(slugs: list[str]) -> str:
    return SELECTION_TEMPLATE.format(
        generated_at=datetime.now(timezone.utc).isoformat(),
        min_messages=4,
        date_floor="",
        available_slugs=", ".join(slugs),
    )
