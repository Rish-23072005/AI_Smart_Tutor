from fastapi import APIRouter

from app.schemas.ask import AskRequest, AskResponse
from app.services import get_tutor_service

router = APIRouter()
service = get_tutor_service()


@router.post("/", response_model=AskResponse)
async def ask(payload: AskRequest) -> AskResponse:
    return service.handle_question(payload)

