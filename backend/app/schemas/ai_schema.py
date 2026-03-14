"""
AI schemas
"""
from pydantic import BaseModel
from typing import Optional, List


class LevelPredictionRequest(BaseModel):
    quiz_results: List[dict] = []
    self_assessment: Optional[str] = None


class LevelPredictionResponse(BaseModel):
    predicted_level: str
    confidence: float
    details: Optional[dict] = None


class RoadmapRecommendation(BaseModel):
    current_level: str
    target_level: str
    recommended_roadmap_id: Optional[int] = None
    weak_skills: List[str] = []
    suggestions: List[str] = []
    estimated_days: int = 30
