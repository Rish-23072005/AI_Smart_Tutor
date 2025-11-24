from pydantic import BaseModel
from typing import Dict


class TopicProgress(BaseModel):
    accuracy: int
    strength: str


class ProgressResponse(BaseModel):
    progress: Dict[str, TopicProgress]
    agent_recommendation: str
    natural_language_summary: str

