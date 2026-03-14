"""
Lesson schemas
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LessonBase(BaseModel):
    title: str
    description: Optional[str] = None
    content: Optional[str] = None
    level: str
    category: Optional[str] = None
    duration_minutes: int = 30


class LessonCreate(LessonBase):
    pass


class LessonUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    level: Optional[str] = None
    category: Optional[str] = None
    duration_minutes: Optional[int] = None
    is_published: Optional[bool] = None


class LessonResponse(LessonBase):
    id: int
    order_index: int
    is_published: bool
    thumbnail_url: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
