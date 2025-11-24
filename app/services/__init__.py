from functools import lru_cache

from .tutor_service import AgenticTutorService


@lru_cache
def get_tutor_service() -> AgenticTutorService:
    return AgenticTutorService()


__all__ = ["AgenticTutorService", "get_tutor_service"]

