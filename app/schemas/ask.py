from pydantic import BaseModel, Field
from typing import List


class QuizQuestion(BaseModel):
    id: int
    question: str
    difficulty: str = Field("easy", description="easy|medium|hard")


class AskRequest(BaseModel):
    question: str
    topic: str | None = None
    subject: str | None = None
    student_id: str | None = None


class AskResponse(BaseModel):
    plan_executed: List[str]
    retrieved_content: str
    quiz: List[QuizQuestion]
    natural_language_response: str

