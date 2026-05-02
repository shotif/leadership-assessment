"""Read a Claude data export (.dms / .zip / unpacked folder) into models."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path
from typing import Any

from .models import (
    Conversation,
    KnowledgeDoc,
    Project,
)

# Files we expect to find inside an export. Names have shifted between
# export generations, so we look up by basename and accept any of these.
CONVERSATION_FILE_NAMES = {"conversations.json"}
PROJECT_FILE_NAMES = {"projects.json"}
USER_FILE_NAMES = {"users.json"}
MEMORIES_FILE_NAMES = {"memories.json"}
# Newer exports place one JSON per project under a "projects/" directory.
PROJECT_DIR_NAME = "projects"


class ParseError(RuntimeError):
    pass


class Export:
    """Parsed contents of an export."""

    def __init__(
        self,
        source: Path,
        projects: list[Project],
        conversations: list[Conversation],
        loose_knowledge_files: dict[str, bytes],
        raw_files: dict[str, int],
        memories: Any | None = None,
    ) -> None:
        self.source = source
        self.projects = projects
        self.conversations = conversations
        # filename -> raw bytes for knowledge files found alongside the
        # JSON (not embedded in projects.json).
        self.loose_knowledge_files = loose_knowledge_files
        # Inventory of every file in the archive (path -> size) for debugging.
        self.raw_files = raw_files
        # Raw memories.json contents if present (used for memory-seed in P3).
        self.memories = memories


def _read_archive(path: Path) -> dict[str, bytes]:
    """Return {member_path: bytes} for every file in the zip."""
    if not path.is_file():
        raise ParseError(f"Not a file: {path}")
    try:
        with zipfile.ZipFile(path) as zf:
            return {
                info.filename: zf.read(info)
                for info in zf.infolist()
                if not info.is_dir()
            }
    except zipfile.BadZipFile as exc:
        raise ParseError(
            f"{path} is not a valid zip archive. "
            "The .dms export should be a renamed ZIP."
        ) from exc


def _read_directory(path: Path) -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    for p in path.rglob("*"):
        if p.is_file():
            out[str(p.relative_to(path))] = p.read_bytes()
    return out


def _load_json(blob: bytes, label: str) -> Any:
    try:
        return json.loads(blob)
    except json.JSONDecodeError as exc:
        raise ParseError(f"Could not parse {label}: {exc}") from exc


def parse_export(path: Path) -> Export:
    """Parse the export at *path* (file or directory)."""
    if path.is_dir():
        files = _read_directory(path)
    else:
        files = _read_archive(path)

    by_basename: dict[str, list[str]] = {}
    for member in files:
        by_basename.setdefault(Path(member).name, []).append(member)

    def _pick(candidates: set[str]) -> str | None:
        for name in candidates:
            if name in by_basename:
                # Prefer the shallowest path if duplicated.
                paths = sorted(by_basename[name], key=lambda p: p.count("/"))
                return paths[0]
        return None

    conv_member = _pick(CONVERSATION_FILE_NAMES)
    if not conv_member:
        raise ParseError(
            "conversations.json not found in the export. "
            f"Files seen: {sorted(by_basename)[:20]}"
        )

    conv_raw = _load_json(files[conv_member], "conversations.json")
    if not isinstance(conv_raw, list):
        raise ParseError("conversations.json is not a JSON array")
    conversations = [Conversation.model_validate(c) for c in conv_raw]

    proj_member = _pick(PROJECT_FILE_NAMES)
    projects: list[Project] = []
    project_member_paths: set[str] = set()
    if proj_member:
        proj_raw = _load_json(files[proj_member], "projects.json")
        if isinstance(proj_raw, list):
            projects = [Project.model_validate(p) for p in proj_raw]
            project_member_paths.add(proj_member)

    # Newer export: one file per project under projects/.
    if not projects:
        for member, blob in files.items():
            parts = Path(member).parts
            if (
                len(parts) >= 2
                and parts[0] == PROJECT_DIR_NAME
                and member.endswith(".json")
            ):
                try:
                    raw = _load_json(blob, member)
                except ParseError:
                    continue
                if isinstance(raw, dict) and raw.get("uuid"):
                    projects.append(Project.model_validate(raw))
                    project_member_paths.add(member)

    # Reconstruct projects from conversations as a last resort.
    if not projects:
        seen: dict[str, Project] = {}
        for c in conversations:
            pid = c.project_id()
            if not pid:
                continue
            if pid not in seen:
                name = c.project.name if c.project and c.project.name else ""
                seen[pid] = Project(uuid=pid, name=name or pid[:8])
        projects = list(seen.values())

    memories_member = _pick(MEMORIES_FILE_NAMES)
    memories: Any | None = None
    if memories_member:
        try:
            memories = _load_json(files[memories_member], "memories.json")
        except ParseError:
            memories = None

    # Loose knowledge files: anything alongside the JSON that isn't itself
    # one of the manifest files. Common layouts include a per-project
    # subdirectory or a top-level "files/" folder.
    skip_basenames = set(
        CONVERSATION_FILE_NAMES | PROJECT_FILE_NAMES | USER_FILE_NAMES | MEMORIES_FILE_NAMES
    )
    loose: dict[str, bytes] = {}
    for member, blob in files.items():
        base = Path(member).name
        if base in skip_basenames:
            continue
        if base.startswith("."):
            continue
        if member in project_member_paths:
            continue
        loose[member] = blob

    raw_inventory = {m: len(b) for m, b in files.items()}
    return Export(
        source=path,
        projects=projects,
        conversations=conversations,
        loose_knowledge_files=loose,
        raw_files=raw_inventory,
        memories=memories,
    )


def slugify(text: str, fallback: str = "untitled") -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]+", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:60] or fallback


def attach_knowledge_to_projects(
    projects: list[Project], loose_files: dict[str, bytes]
) -> dict[str, list[tuple[str, int]]]:
    """Best-effort association of loose files to projects.

    Returns a map of project_uuid -> list of (member_path, size_bytes) for
    files that look like they belong to that project (path contains the
    project uuid or a slug of its name). Files that don't match any project
    are returned under the empty-string key.
    """
    result: dict[str, list[tuple[str, int]]] = {p.uuid: [] for p in projects}
    result[""] = []
    name_slugs = {slugify(p.name): p.uuid for p in projects if p.name}

    for member, blob in loose_files.items():
        member_lower = member.lower()
        matched: str | None = None
        for p in projects:
            if p.uuid and p.uuid.lower() in member_lower:
                matched = p.uuid
                break
        if matched is None:
            for slug, pid in name_slugs.items():
                if slug and slug in member_lower:
                    matched = pid
                    break
        result.setdefault(matched or "", []).append((member, len(blob)))
    return result
