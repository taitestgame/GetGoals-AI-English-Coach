"""
AI routes - AI prediction and recommendation endpoints
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.models.user import User
from app.schemas.ai_schema import LevelPredictionRequest, LevelPredictionResponse, RoadmapRecommendation
from app.services.ai_service import AIService

router = APIRouter()


@router.post("/predict-level", response_model=LevelPredictionResponse)
async def predict_level(
    request: LevelPredictionRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Predict user's English level using AI"""
    service = AIService(db)
    return service.predict_level(current_user.id, request)


@router.get("/recommendation", response_model=RoadmapRecommendation)
async def get_recommendation(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Get AI-powered learning roadmap recommendation"""
    service = AIService(db)
    return service.get_recommendation(current_user.id)


@router.get("/weak-skills")
async def get_weak_skills(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Get user's weak skills analysis"""
    service = AIService(db)
    return service.analyze_weak_skills(current_user.id)
