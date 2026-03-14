"""
Quiz model
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    level = Column(String(20), nullable=False)
    quiz_type = Column(String(50), nullable=False)  # multiple_choice, fill_in, matching, listening
    questions = Column(JSON, nullable=True)  # JSON array of questions
    time_limit_minutes = Column(Integer, default=15)
    passing_score = Column(Integer, default=60)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
