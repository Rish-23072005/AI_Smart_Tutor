from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="Agentic AI Tutor")
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)
    streamlit_port: int = Field(default=8501)
    database_url: str = Field(default="sqlite:///./app.db")
    kb_source_dir: str = Field(default="./data/source_materials")
    kb_embeddings_dir: str = Field(default="./embeddings")
    embedding_model: str = Field(default="sentence-transformers/all-MiniLM-L6-v2")
    openai_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()

