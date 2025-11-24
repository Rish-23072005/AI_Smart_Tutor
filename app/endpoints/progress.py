from fastapi import APIRouter

from app.schemas.progress import ProgressResponse
from app.services import get_tutor_service

router = APIRouter()
service = get_tutor_service()


@router.get("/{student_id}", response_model=ProgressResponse)
async def progress(student_id: str) -> ProgressResponse:
    return service.get_progress(student_id)

