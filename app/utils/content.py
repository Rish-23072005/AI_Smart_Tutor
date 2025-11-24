from __future__ import annotations

from textwrap import dedent


def build_topic_brief(topic: str, subject: str | None = None) -> str:
    """Return a structured overview for arbitrary topics."""
    cleaned_topic = topic.strip().title() or "This Topic"
    subject_label = subject.strip().title() if subject else "General Studies"

    overview = dedent(
        f"""
        {cleaned_topic} — {subject_label} Overview
        Definition:
          • Explain the core idea of {cleaned_topic}. State what it represents in {subject_label}
            and why it matters for competitive exams.

        Core Concepts:
          • Outline foundational principles, formulas, or rules tied to {cleaned_topic}.
          • Highlight at least one worked example to show how the concept is applied.

        Study Workflow:
          1. Review prerequisite knowledge for {subject_label}.
          2. Break {cleaned_topic} into micro-skills (theory, procedure, edge cases).
          3. Practice progressively; start with easy identification questions, then pivot to mixed reasoning.

        Common Pitfalls:
          • Misinterpreting definitions or conditions.
          • Forgetting to check domain/units/assumptions.
          • Skipping reflection after solving problems, which limits retention.

        Active Recall Ideas:
          • Create a flashcard that states the definition on one side and a real-world scenario on the other.
          • Derive the main formula or workflow from memory, then verify against notes.

        Next Steps:
          • Attempt 3–5 targeted practice questions at increasing difficulty.
          • Summarize insights gained and update the progress tracker.
        """
    ).strip()

    return overview

