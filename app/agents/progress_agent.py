from __future__ import annotations

from typing import Dict


class ProgressTrackerAgent:
    def __init__(self) -> None:
        self._store: Dict[str, Dict[str, dict]] = {}

    def get_progress(self, student_id: str) -> Dict[str, dict]:
        if student_id not in self._store:
            self._store[student_id] = {
                "Probability": {"accuracy": 55, "strength": "weak"},
                "Algebra": {"accuracy": 90, "strength": "strong"},
            }
        return self._store[student_id]

    def update_topic(self, student_id: str, topic: str, accuracy: int) -> None:
        progress = self.get_progress(student_id)
        progress[topic] = {
            "accuracy": accuracy,
            "strength": "strong" if accuracy >= 70 else "weak",
        }

