"""Phase 3 build — materialize the migration kit on disk.

Mechanical work only: directory structure, instructions, knowledge files,
conversation transcripts, README, and skeleton files for context-digest /
memory-seed / settings-checklist (filled in by a follow-up step that uses
the API or an in-chat run).
"""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .models import Conversation, ConversationSummary, Project
from .parser import slugify


# Noise the export interleaves into transcripts when Claude was using tools.
# These never carry signal worth preserving in the rebuild kit.
NOISE_PATTERNS = [
    re.compile(
        r"```\n?This block is not supported on your current device yet\.\n?```",
        re.DOTALL,
    ),
]


def clean_message_text(text: str) -> str:
    s = text or ""
    for pat in NOISE_PATTERNS:
        s = pat.sub("", s)
    # Collapse 3+ blank lines that the substitution may leave behind.
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def fmt_dt(dt: datetime | None) -> str:
    if dt is None:
        return "—"
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat()


def fmt_date(dt: datetime | None) -> str:
    if dt is None:
        return "—"
    return dt.date().isoformat()


def render_conversation(conv: Conversation) -> str:
    parts: list[str] = []
    parts.append(f"# {conv.name or '(untitled)'}\n")
    parts.append(
        "- **Conversation ID:** `{uuid}`\n"
        "- **Created:** {created}\n"
        "- **Updated:** {updated}\n"
        "- **Messages:** {msgs}\n".format(
            uuid=conv.uuid,
            created=fmt_dt(conv.created_at),
            updated=fmt_dt(conv.updated_at),
            msgs=len(conv.chat_messages),
        )
    )
    parts.append("\n---\n")
    for m in conv.chat_messages:
        sender = (m.sender or "unknown").strip().lower()
        label = {"human": "Human", "assistant": "Assistant"}.get(sender, sender.title())
        ts = fmt_dt(m.created_at)
        body = clean_message_text(m.plain_text())
        if not body:
            continue
        parts.append(f"\n## {label}  *({ts})*\n\n{body}\n")
    return "".join(parts)


def conversation_slug(conv_summary: ConversationSummary, used: set[str]) -> str:
    base = slugify(conv_summary.title) or conv_summary.uuid[:8]
    candidate = base
    i = 2
    while candidate in used:
        candidate = f"{base}-{i}"
        i += 1
    used.add(candidate)
    return candidate


def safe_filename(name: str) -> str:
    """Make a filename safe across filesystems while keeping it readable."""
    s = unicodedata.normalize("NFKC", name)
    # Strip path separators and other unsafe chars but keep extension dots.
    s = re.sub(r"[\\/\x00-\x1f]+", "_", s)
    s = s.strip(" .")
    return s or "file"


def write_project(
    out_dir: Path,
    project: Project,
    project_slug: str,
    kept_conversations: list[Conversation],
    knowledge_files_from_archive: list[tuple[str, bytes]] | None = None,
    project_memory: str | None = None,
) -> Path:
    """Write the per-project subtree. Returns the project directory."""
    proj_dir = out_dir / "projects" / project_slug
    (proj_dir / "knowledge").mkdir(parents=True, exist_ok=True)
    (proj_dir / "conversations").mkdir(parents=True, exist_ok=True)

    # instructions.md — verbatim, or a placeholder so the file always exists.
    instr = (project.prompt_template or "").strip()
    instructions_md = (
        f"# Custom instructions — {project.name or project_slug}\n\n"
        + (instr if instr else "_(No custom instructions set on the original project.)_")
        + "\n"
    )
    (proj_dir / "instructions.md").write_text(instructions_md, encoding="utf-8")

    # knowledge/ — embedded docs from the project JSON.
    for doc in project.docs:
        if not doc.content:
            continue
        fname = safe_filename(doc.name)
        (proj_dir / "knowledge" / fname).write_text(doc.content, encoding="utf-8")
    # plus any loose files associated with the project.
    if knowledge_files_from_archive:
        for member_path, blob in knowledge_files_from_archive:
            fname = safe_filename(Path(member_path).name)
            (proj_dir / "knowledge" / fname).write_bytes(blob)

    # conversations/ — clean markdown.
    used: set[str] = set()
    rendered: list[tuple[str, ConversationSummary]] = []
    for conv in kept_conversations:
        cs = ConversationSummary(
            uuid=conv.uuid,
            title=conv.name or "(untitled)",
            project_uuid=conv.project_id(),
            message_count=len(conv.chat_messages),
            first_message_at=conv.created_at,
            last_message_at=conv.updated_at or conv.created_at,
            char_count=sum(len(m.plain_text()) for m in conv.chat_messages),
            estimated_tokens=0,
        )
        cslug = conversation_slug(cs, used)
        (proj_dir / "conversations" / f"{cslug}.md").write_text(
            render_conversation(conv), encoding="utf-8"
        )
        rendered.append((cslug, cs))

    # context-digest.md placeholder — will be replaced by the synthesis step.
    digest_md = (
        f"# Context digest — {project.name or project_slug}\n\n"
        "_This file will be filled in by the synthesis step "
        "(API call or in-chat run)._\n\n"
        "## Source material\n\n"
        f"- {len(rendered)} kept conversations under `conversations/`.\n"
        f"- {len(project.docs)} embedded knowledge files under `knowledge/`.\n"
    )
    if project_memory:
        digest_md += (
            "\n## Project memory (from `memories.json`)\n\n"
            "Verbatim, for reference while writing the digest:\n\n"
            "```\n" + project_memory.strip() + "\n```\n"
        )
    (proj_dir / "context-digest.md").write_text(digest_md, encoding="utf-8")

    return proj_dir


def write_standalone(
    out_dir: Path, conv: Conversation, used: set[str]
) -> str:
    cs = ConversationSummary(
        uuid=conv.uuid,
        title=conv.name or "(untitled)",
        project_uuid=None,
        message_count=len(conv.chat_messages),
        first_message_at=conv.created_at,
        last_message_at=conv.updated_at or conv.created_at,
        char_count=0,
        estimated_tokens=0,
    )
    slug = conversation_slug(cs, used)
    standalone_dir = out_dir / "standalone"
    standalone_dir.mkdir(parents=True, exist_ok=True)
    (standalone_dir / f"{slug}.md").write_text(
        render_conversation(conv), encoding="utf-8"
    )
    return slug


def render_readme(
    out_dir: Path,
    project_dirs: list[tuple[str, Path, int]],
    standalone_count: int,
    has_memory_seed: bool,
) -> str:
    lines: list[str] = []
    lines.append("# Migration kit\n")
    lines.append(
        "Manual rebuild kit for an Enterprise Claude account. Generated by "
        "`claude-migration-kit build`.\n"
    )
    lines.append(
        "\n## Rebuild order\n\n"
        "1. **Sign in** to the new Enterprise account.\n"
        "2. **Recreate the projects** below — for each, copy `instructions.md` "
        "into the project's custom instructions and upload everything from "
        "`knowledge/` as project knowledge.\n"
        "3. **Seed memory** by pasting `memory-seed.md` into a fresh chat with "
        "the request \"add this as standing context for our future conversations.\"\n"
        "4. **Recreate settings** manually using `settings-checklist.md`.\n"
        "5. **Use `context-digest.md` per project** as your own primer when you "
        "next pick the project up — paste it into the first chat in that project.\n"
        "6. The full transcripts under `conversations/` and `standalone/` are "
        "for your reference. They are *not* meant to be replayed into "
        "Enterprise; they document what was discussed and decided.\n"
    )

    lines.append("\n## What's included\n")
    if project_dirs:
        lines.append("\n### Projects\n")
        for slug, _, conv_count in project_dirs:
            lines.append(
                f"- `projects/{slug}/` — {conv_count} kept conversation"
                f"{'s' if conv_count != 1 else ''}\n"
            )
    if standalone_count:
        lines.append(
            f"\n### Standalone\n\n- `standalone/` — {standalone_count} kept "
            "non-project conversations\n"
        )
    if has_memory_seed:
        lines.append("\n### Cross-cutting\n\n- `memory-seed.md`\n- `settings-checklist.md`\n")

    lines.append(
        "\n## Notes\n\n"
        "- Generated from a Claude data export. Conversation transcripts "
        "include only `human` / `assistant` text turns; tool use and "
        "rendered artifacts are not preserved.\n"
        "- The `coaching` project (if it existed) is excluded by default "
        "because it contains personal content.\n"
    )
    return "".join(lines)


def render_settings_checklist(memories: Any | None) -> str:
    lines: list[str] = [
        "# Settings checklist\n",
        "\nThings to recreate manually in the Enterprise UI. Anthropic's API "
        "doesn't expose these, so they need to be re-set by hand.\n",
        "\n## Account\n",
        "- [ ] Display name and avatar\n",
        "- [ ] Default response language preference\n",
        "- [ ] Personal preferences / response style (concise, formal, etc.)\n",
        "\n## Connectors\n",
        "- [ ] Re-authorize any MCP / connector integrations from the source "
        "account (Google Drive, GitHub, etc.). Anthropic does not transfer "
        "OAuth grants between accounts.\n",
        "\n## Custom styles\n",
        "- [ ] Recreate any custom writing styles you'd defined.\n",
        "\n## Skills\n",
        "- [ ] Re-upload any custom skills you used (e.g. T-Brand designer, "
        "skill-creator). Source skill files are not in the export.\n",
        "\n## Projects\n",
        "- [ ] For each project under `projects/`, copy `instructions.md` "
        "into the new project's custom instructions and upload `knowledge/`.\n",
        "\n## Memory\n",
        "- [ ] Paste `memory-seed.md` into a fresh Enterprise chat with the "
        "instruction: *\"Save this as standing memory for future conversations.\"*\n",
        "- [ ] (Optional) For projects with rich pre-existing memory, paste "
        "the project's `context-digest.md` into the first chat under that "
        "project to prime its memory.\n",
    ]
    return "".join(lines)
