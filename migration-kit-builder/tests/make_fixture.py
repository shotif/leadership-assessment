"""Build a small synthetic Claude-style export for smoke tests."""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path


def build(out: Path) -> None:
    projects = [
        {
            "uuid": "proj-aaa",
            "name": "Strategy Notes",
            "description": "Long-running strategy thinking",
            "prompt_template": "You are a strategy partner. Be terse.",
            "created_at": "2025-01-04T10:00:00Z",
            "docs": [
                {
                    "uuid": "doc-1",
                    "filename": "okrs.md",
                    "content": "# OKRs Q1\n- Ship migration kit\n",
                    "created_at": "2025-01-05T10:00:00Z",
                }
            ],
        },
        {
            "uuid": "proj-bbb",
            "name": "Vacation Planning",
            "description": "",
            "prompt_template": "",
            "created_at": "2024-12-01T10:00:00Z",
            "docs": [],
        },
    ]
    conversations = [
        {
            "uuid": "conv-1",
            "name": "Q1 strategy framing",
            "created_at": "2025-01-10T10:00:00Z",
            "updated_at": "2025-01-12T10:00:00Z",
            "project_uuid": "proj-aaa",
            "chat_messages": [
                {
                    "uuid": "m1",
                    "sender": "human",
                    "text": "Help me frame Q1 OKRs.",
                    "created_at": "2025-01-10T10:00:00Z",
                },
                {
                    "uuid": "m2",
                    "sender": "assistant",
                    "text": "Three pillars: ship, measure, learn.",
                    "created_at": "2025-01-10T10:01:00Z",
                },
            ],
        },
        {
            "uuid": "conv-2",
            "name": "Croatia road trip",
            "created_at": "2024-12-10T10:00:00Z",
            "updated_at": "2024-12-10T11:00:00Z",
            "project_uuid": "proj-bbb",
            "chat_messages": [
                {
                    "uuid": "m3",
                    "sender": "human",
                    "text": "Best route Zagreb to Split?",
                    "created_at": "2024-12-10T10:00:00Z",
                }
            ],
        },
        {
            "uuid": "conv-3",
            "name": "One-off Python question",
            "created_at": "2025-02-01T10:00:00Z",
            "updated_at": "2025-02-01T10:00:00Z",
            "chat_messages": [
                {
                    "uuid": "m4",
                    "sender": "human",
                    "text": "How do I read JSON in Python?",
                    "created_at": "2025-02-01T10:00:00Z",
                },
                {
                    "uuid": "m5",
                    "sender": "assistant",
                    "text": "Use json.loads or json.load.",
                    "created_at": "2025-02-01T10:01:00Z",
                },
            ],
        },
    ]

    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w") as zf:
        zf.writestr("conversations.json", json.dumps(conversations))
        zf.writestr("projects.json", json.dumps(projects))
        zf.writestr(
            "files/proj-aaa/okrs.md",
            "# OKRs Q1\n- Ship migration kit\n",
        )


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("fixture.dms")
    build(target)
    print(f"Wrote {target}")
