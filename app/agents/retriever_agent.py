from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class KnowledgeBase(Protocol):
    def fetch(self, topic: str, subject: str | None = None) -> str: ...


@dataclass
class RetrieverAgent:
    knowledge_base: KnowledgeBase

    def retrieve(self, topic: str, subject: str | None = None) -> str:
        return self.knowledge_base.fetch(topic, subject)

