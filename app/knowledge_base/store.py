from __future__ import annotations

from typing import Dict

from app.utils.content import build_topic_brief


class InMemoryKnowledgeBase:
    def __init__(self) -> None:
        self._store: Dict[str, str] = {
            "probability": (
                "Conditional probability measures the likelihood of event A occurring "
                "given that event B already occurred. Formula: P(A|B) = P(A ∩ B) / P(B) "
                "whenever P(B) > 0. Remember to identify the overlap of events, ensure "
                "the conditioning event has non-zero probability, and reduce fractions."
            ),
            "algebra": (
                "Algebra manipulates symbols and letters to solve equations and understand structures."
            ),
            "calculus": (
                "Calculus studies rates of change (derivatives) and accumulation (integrals)."
            ),
        }

    def fetch(self, topic: str, subject: str | None = None) -> str:
        key = self._normalize(topic)
        if key not in self._store:
            self._store[key] = build_topic_brief(topic, subject)
        return self._store[key]

    def upsert(self, topic: str, content: str) -> None:
        self._store[self._normalize(topic)] = content

    def _normalize(self, value: str) -> str:
        return value.strip().lower()

