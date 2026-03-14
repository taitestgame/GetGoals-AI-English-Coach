"""
Roadmap model
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON, Float
from sqlalchemy.sql import func
from app.core.database import Base


class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    target_level = Column(String(20), nullable=False)  # A1->A2, B1->B2, etc.
    estimated_days = Column(Integer, default=30)
    milestones = Column(JSON, nullable=True)  # JSON array of milestones
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class UserRoadmap(Base):
    __tablename__ = "user_roadmaps"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    roadmap_id = Column(Integer, ForeignKey("roadmaps.id"), nullable=False)
    progress = Column(Float, default=0.0)  # 0-100 percentage
    current_milestone = Column(Integer, default=0)
    status = Column(String(20), default="active")  # active, completed, paused
    started_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime, nullable=True)
