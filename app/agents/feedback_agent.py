class FeedbackAgent:
    def summarize(
        self,
        topic: str,
        subject: str | None,
        difficulty: str,
        num_questions: int = 2,
    ) -> str:
        subject_fragment = subject or "this subject"
        return (
            f"I noticed you're exploring {topic} in {subject_fragment}. "
            f"We'll review the key ideas and tackle {num_questions} {difficulty} questions "
            "to reinforce understanding."
        )

