from pydantic import BaseModel, Field
from typing import List


class QuizRequest(BaseModel):
    topic: str
    difficulty: str = Field("medium", pattern="^(easy|medium|hard)$")
    num_questions: int = Field(3, ge=1, le=10)
    subject: str | None = None
    student_id: str | None = None


class QuizQuestion(BaseModel):
    id: int
    question: str
    difficulty: str


class QuizResponse(BaseModel):
    topic: str
    difficulty: str
    questions: List[QuizQuestion]

