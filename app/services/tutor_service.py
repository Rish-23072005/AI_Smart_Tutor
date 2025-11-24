from __future__ import annotations

from app.agents import (
    FeedbackAgent,
    PlannerAgent,
    ProgressTrackerAgent,
    QuizGeneratorAgent,
    RetrieverAgent,
)
from app.knowledge_base import InMemoryKnowledgeBase
from app.schemas.ask import AskRequest, AskResponse, QuizQuestion as AskQuizQuestion
from app.schemas.quiz import QuizRequest, QuizResponse, QuizQuestion
from app.schemas.progress import ProgressResponse


class AgenticTutorService:
    def __init__(self) -> None:
        knowledge_base = InMemoryKnowledgeBase()
        self.progress_tracker = ProgressTrackerAgent()
        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent(knowledge_base=knowledge_base)
        self.quiz_generator = QuizGeneratorAgent()
        self.feedback_agent = FeedbackAgent()

    def handle_question(self, payload: AskRequest) -> AskResponse:
        student_id = payload.student_id or "anonymous"
        profile = self.progress_tracker.get_progress(student_id)
        planner_output = self.planner.plan(
            profile,
            payload.question,
            explicit_topic=payload.topic,
            subject=payload.subject,
        )
        content = self.retriever.retrieve(
            planner_output.topic, planner_output.subject or payload.subject
        )
        num_quiz_questions = 2
        quiz_questions = self.quiz_generator.generate(
            topic=planner_output.topic,
            difficulty=planner_output.difficulty,
            num_questions=num_quiz_questions,
            subject=planner_output.subject or payload.subject,
        )
        response = AskResponse(
            plan_executed=planner_output.plan_steps,
            retrieved_content=content,
            quiz=[AskQuizQuestion(**question) for question in quiz_questions],
            natural_language_response=self.feedback_agent.summarize(
                planner_output.topic,
                planner_output.subject or payload.subject,
                planner_output.difficulty,
                num_questions=num_quiz_questions,
            ),
        )
        return response

    def generate_quiz(self, payload: QuizRequest) -> QuizResponse:
        questions = self.quiz_generator.generate(
            topic=payload.topic,
            difficulty=payload.difficulty,
            num_questions=payload.num_questions,
            subject=payload.subject,
        )
        quiz_questions = [QuizQuestion(**question) for question in questions]
        return QuizResponse(
            topic=payload.topic, difficulty=payload.difficulty, questions=quiz_questions
        )

    def get_progress(self, student_id: str) -> ProgressResponse:
        progress = self.progress_tracker.get_progress(student_id)
        recommendation = f"Focus next on {self._weakest_topic(progress)}."
        summary = (
            "You're progressing well. We'll continue reinforcing weak topics "
            "while keeping strong areas sharp."
        )
        return ProgressResponse(
            progress=progress,
            agent_recommendation=recommendation,
            natural_language_summary=summary,
        )

    def _weakest_topic(self, progress: dict) -> str:
        return min(progress.items(), key=lambda item: item[1]["accuracy"])[0]

