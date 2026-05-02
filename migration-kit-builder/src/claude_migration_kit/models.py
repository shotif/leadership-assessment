"""Pydantic data model for the Claude export.

The export schema is not formally documented and varies between exports.
Models are deliberately tolerant: unknown fields are ignored, and most
fields are optional. Adjust as needed once a real export is parsed.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ExportBase(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)


class KnowledgeDoc(ExportBase):
    uuid: str | None = None
    filename: str | None = None
    file_name: str | None = None
    content: str | None = None
    created_at: datetime | None = None

    @property
    def name(self) -> str:
        return self.filename or self.file_name or self.uuid or "unnamed"


class Project(ExportBase):
    uuid: str
    name: str = ""
    description: str | None = None
    prompt_template: str | None = None
    is_starter_project: bool | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    docs: list[KnowledgeDoc] = Field(default_factory=list)


class Attachment(ExportBase):
    file_name: str | None = None
    file_size: int | None = None
    file_type: str | None = None
    extracted_content: str | None = None


class MessageContentBlock(ExportBase):
    type: str | None = None
    text: str | None = None


class ChatMessage(ExportBase):
    uuid: str | None = None
    text: str | None = None
    content: list[MessageContentBlock] = Field(default_factory=list)
    sender: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    attachments: list[Attachment] = Field(default_factory=list)
    files: list[dict[str, Any]] = Field(default_factory=list)

    def plain_text(self) -> str:
        if self.text:
            return self.text
        parts: list[str] = []
        for block in self.content:
            if block.text:
                parts.append(block.text)
        return "\n".join(parts)


class ConversationProjectRef(ExportBase):
    uuid: str | None = None
    name: str | None = None


class Conversation(ExportBase):
    uuid: str
    name: str = ""
    created_at: datetime | None = None
    updated_at: datetime | None = None
    chat_messages: list[ChatMessage] = Field(default_factory=list)
    project_uuid: str | None = None
    project: ConversationProjectRef | None = None

    def project_id(self) -> str | None:
        if self.project_uuid:
            return self.project_uuid
        if self.project and self.project.uuid:
            return self.project.uuid
        return None


class ConversationSummary(BaseModel):
    """One row in the inventory."""

    uuid: str
    title: str
    project_uuid: str | None
    message_count: int
    first_message_at: datetime | None
    last_message_at: datetime | None
    char_count: int
    estimated_tokens: int


class KnowledgeFileSummary(BaseModel):
    filename: str
    size_bytes: int
    source: str  # "embedded" or path inside the export


class ProjectSummary(BaseModel):
    uuid: str
    slug: str
    name: str
    description: str | None
    has_instructions: bool
    instructions_chars: int
    knowledge_files: list[KnowledgeFileSummary]
    conversations: list[ConversationSummary]


class Inventory(BaseModel):
    export_path: str
    generated_at: datetime
    projects: list[ProjectSummary]
    standalone_conversations: list[ConversationSummary]
    totals: dict[str, int]
