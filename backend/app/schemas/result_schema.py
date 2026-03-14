"""
Result schemas
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ResultResponse(BaseModel):
    id: int
    user_id: int
    quiz_id: int
    score: float
    total_questions: int
    correct_answers: int
    time_spent_seconds: Optional[int] = None
    feedback: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
