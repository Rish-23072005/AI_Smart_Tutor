from sqlalchemy import Column, Integer, String

from app.database import Base


class StudentProgress(Base):
    __tablename__ = "student_progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True, nullable=False)
    topic = Column(String, nullable=False)
    accuracy = Column(Integer, nullable=False, default=0)
    strength = Column(String, nullable=False, default="weak")

