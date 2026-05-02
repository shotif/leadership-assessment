"""Build a Phase-1 inventory from a parsed export."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .models import (
    Conversation,
    ConversationSummary,
    Inventory,
    KnowledgeFileSummary,
    Project,
    ProjectSummary,
)
from .parser import Export, attach_knowledge_to_projects, slugify


def estimate_tokens(char_count: int) -> int:
    # Very rough heuristic: ~4 chars per token for English-ish text.
    # Not API-accurate but fine for ordering and ballpark cost.
    return max(0, char_count // 4)


def summarize_conversation(c: Conversation) -> ConversationSummary:
    char_count = 0
    first: datetime | None = None
    last: datetime | None = None
    for m in c.chat_messages:
        char_count += len(m.plain_text())
        if m.created_at:
            if first is None or m.created_at < first:
                first = m.created_at
            if last is None or m.created_at > last:
                last = m.created_at
    if first is None:
        first = c.created_at
    if last is None:
        last = c.updated_at or c.created_at
    return ConversationSummary(
        uuid=c.uuid,
        title=c.name or "(untitled)",
        project_uuid=c.project_id(),
        message_count=len(c.chat_messages),
        first_message_at=first,
        last_message_at=last,
        char_count=char_count,
        estimated_tokens=estimate_tokens(char_count),
    )


def build_inventory(export: Export) -> Inventory:
    convs_by_project: dict[str | None, list[ConversationSummary]] = {}
    for c in export.conversations:
        s = summarize_conversation(c)
        convs_by_project.setdefault(s.project_uuid, []).append(s)

    knowledge_by_project = attach_knowledge_to_projects(
        export.projects, export.loose_knowledge_files
    )

    used_slugs: set[str] = set()

    def unique_slug(base: str) -> str:
        slug = slugify(base)
        candidate = slug
        i = 2
        while candidate in used_slugs:
            candidate = f"{slug}-{i}"
            i += 1
        used_slugs.add(candidate)
        return candidate

    project_summaries: list[ProjectSummary] = []
    for p in sorted(export.projects, key=lambda x: x.name.lower()):
        knowledge: list[KnowledgeFileSummary] = []
        for doc in p.docs:
            content = doc.content or ""
            knowledge.append(
                KnowledgeFileSummary(
                    filename=doc.name,
                    size_bytes=len(content.encode("utf-8")),
                    source="embedded",
                )
            )
        for member, size in knowledge_by_project.get(p.uuid, []):
            knowledge.append(
                KnowledgeFileSummary(
                    filename=Path(member).name,
                    size_bytes=size,
                    source=member,
                )
            )

        instr = p.prompt_template or ""
        project_summaries.append(
            ProjectSummary(
                uuid=p.uuid,
                slug=unique_slug(p.name or p.uuid[:8]),
                name=p.name or "(untitled)",
                description=p.description,
                has_instructions=bool(instr.strip()),
                instructions_chars=len(instr),
                knowledge_files=knowledge,
                conversations=sorted(
                    convs_by_project.get(p.uuid, []),
                    key=lambda c: c.last_message_at or datetime.min.replace(
                        tzinfo=timezone.utc
                    ),
                    reverse=True,
                ),
            )
        )

    standalone = sorted(
        convs_by_project.get(None, []),
        key=lambda c: c.last_message_at or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )

    total_msgs = sum(c.message_count for c in standalone) + sum(
        cs.message_count for p in project_summaries for cs in p.conversations
    )
    total_tokens = sum(c.estimated_tokens for c in standalone) + sum(
        cs.estimated_tokens for p in project_summaries for cs in p.conversations
    )

    return Inventory(
        export_path=str(export.source),
        generated_at=datetime.now(timezone.utc),
        projects=project_summaries,
        standalone_conversations=standalone,
        totals={
            "projects": len(project_summaries),
            "conversations": len(export.conversations),
            "standalone_conversations": len(standalone),
            "messages": total_msgs,
            "estimated_tokens": total_tokens,
        },
    )
