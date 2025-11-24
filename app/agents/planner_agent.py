from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class PlannerOutput:
    plan_steps: List[str]
    topic: str
    subject: str
    difficulty: str


class PlannerAgent:
    """Decides what to do next based on the current student profile."""

    def plan(
        self,
        student_profile: Dict,
        query: str,
        explicit_topic: str | None = None,
        subject: str | None = None,
    ) -> PlannerOutput:
        topic = explicit_topic or self._infer_topic(query)
        subject = subject or self._infer_subject(topic)
        strength = student_profile.get(topic, {}).get("strength", "weak")
        difficulty = "easy" if strength == "weak" else "medium"
        plan = [
            f"Identified topic: {topic} ({subject})",
            "Retrieved targeted study material",
            "Generated adaptive practice questions",
        ]
        return PlannerOutput(
            plan_steps=plan, topic=topic, subject=subject, difficulty=difficulty
        )

    def _infer_topic(self, query: str) -> str:
        lowered = query.lower()
        if "algebra" in lowered:
            return "Algebra"
        if "calculus" in lowered:
            return "Calculus"
        if "geometry" in lowered:
            return "Geometry"
        return "Probability"

    def _infer_subject(self, topic: str) -> str:
        topic_lower = topic.lower()
        if topic_lower in {"probability", "algebra", "calculus", "geometry"}:
            return "Mathematics"
        if any(word in topic_lower for word in ["physics", "mechanics", "optics"]):
            return "Physics"
        if any(word in topic_lower for word in ["chemistry", "organic", "inorganic"]):
            return "Chemistry"
        if any(word in topic_lower for word in ["biology", "genetics", "cell"]):
            return "Biology"
        return "General Studies"

