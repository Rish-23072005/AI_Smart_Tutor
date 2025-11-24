from __future__ import annotations

from __future__ import annotations

from typing import List

PROBABILITY_QUESTIONS = [
    {
        "id": 1,
        "question": "A coin is tossed twice. What is the probability of exactly one head?",
        "difficulty": "easy",
    },
    {
        "id": 2,
        "question": "If P(A)=0.3 and P(B)=0.5 with P(A∩B)=0.15, what is P(A|B)?",
        "difficulty": "easy",
    },
    {
        "id": 3,
        "question": "A bag has 3 red and 2 blue balls. Draw two without replacement. "
        "What is the chance both are red?",
        "difficulty": "medium",
    },
]


class QuizGeneratorAgent:
    def generate(
        self,
        topic: str,
        difficulty: str,
        num_questions: int,
        subject: str | None = None,
    ) -> List[dict]:
        if topic.lower() == "probability":
            filtered = [
                q
                for q in PROBABILITY_QUESTIONS
                if q["difficulty"] in {difficulty, "easy"}
            ]
            if len(filtered) < num_questions:
                filtered.extend(
                    self._build_generic_questions(
                        topic, subject, difficulty, num_questions - len(filtered), start_id=4
                    )
                )
            return filtered[:num_questions]

        return self._build_generic_questions(topic, subject, difficulty, num_questions)

    def _build_generic_questions(
        self,
        topic: str,
        subject: str | None,
        difficulty: str,
        num_questions: int,
        start_id: int = 1,
    ) -> List[dict]:
        subject_fragment = subject or "your course"
        prompts = {
            "easy": "State the main idea of",
            "medium": "Apply the core rule of",
            "hard": "Synthesize multiple ideas from",
        }
        verb = prompts.get(difficulty, "Discuss")

        return [
            {
                "id": start_id + idx,
                "question": (
                    f"[{difficulty.upper()}] {verb} {topic} within {subject_fragment}. "
                    f"Provide an example or calculation (Question {start_id + idx})."
                ),
                "difficulty": difficulty,
            }
            for idx in range(num_questions)
        ]

