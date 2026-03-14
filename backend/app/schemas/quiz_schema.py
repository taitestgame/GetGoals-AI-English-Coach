"""
Quiz schemas
"""
from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime


class QuizCreate(BaseModel):
    lesson_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    level: str
    quiz_type: str
    questions: List[dict] = []
    time_limit_minutes: int = 15
    passing_score: int = 60


class QuizResponse(BaseModel):
    id: int
    lesson_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    level: str
    quiz_type: str
    questions: Optional[List[dict]] = None
    time_limit_minutes: int
    passing_score: int
    created_at: datetime

    class Config:
        from_attributes = True


class QuizSubmit(BaseModel):
    answers: List[dict]
    time_spent_seconds: Optional[int] = None


class QuizResultResponse(BaseModel):
    quiz_id: int
    score: float
    total_questions: int
    correct_answers: int
    feedback: Optional[str] = None
