from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from app.config import get_settings

Base = declarative_base()


def get_engine():
    settings = get_settings()
    return create_engine(settings.database_url, future=True)


def get_session() -> Session:
    engine = get_engine()
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)()

