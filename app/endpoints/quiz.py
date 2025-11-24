from fastapi import APIRouter

from app.schemas.quiz import QuizRequest, QuizResponse
from app.services import get_tutor_service

router = APIRouter()
service = get_tutor_service()


@router.post("/", response_model=QuizResponse)
async def quiz(payload: QuizRequest) -> QuizResponse:
    return service.generate_quiz(payload)

