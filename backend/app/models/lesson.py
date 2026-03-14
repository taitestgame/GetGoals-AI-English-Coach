"""
Lesson model
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.core.database import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=True)
    level = Column(String(20), nullable=False)  # A1, A2, B1, B2, C1, C2
    category = Column(String(100), nullable=True)  # grammar, vocabulary, reading, listening, speaking, writing
    duration_minutes = Column(Integer, default=30)
    order_index = Column(Integer, default=0)
    is_published = Column(Boolean, default=False)
    thumbnail_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
