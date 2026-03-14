"""
AI service - handles AI predictions and recommendations
"""
from sqlalchemy.orm import Session
from app.models.result import Result
from app.models.user import User
from app.schemas.ai_schema import LevelPredictionRequest, LevelPredictionResponse, RoadmapRecommendation


class AIService:
    def __init__(self, db: Session):
        self.db = db

    def predict_level(self, user_id: int, request: LevelPredictionRequest) -> LevelPredictionResponse:
        """Predict English level using AI model"""
        # TODO: Integrate with AI engine
        # Placeholder logic
        return LevelPredictionResponse(
            predicted_level="B1",
            confidence=0.75,
            details={"message": "Level prediction based on quiz results"},
        )

    def get_recommendation(self, user_id: int) -> RoadmapRecommendation:
        """Get AI-powered roadmap recommendation"""
        user = self.db.query(User).filter(User.id == user_id).first()
        current_level = user.english_level or "A1"

        # TODO: Integrate with AI engine for real recommendations
        level_map = {"A1": "A2", "A2": "B1", "B1": "B2", "B2": "C1", "C1": "C2", "C2": "C2"}
        target_level = level_map.get(current_level, "B1")

        return RoadmapRecommendation(
            current_level=current_level,
            target_level=target_level,
            weak_skills=["grammar", "listening"],
            suggestions=["Focus on grammar exercises", "Practice listening daily"],
            estimated_days=30,
        )

    def analyze_weak_skills(self, user_id: int) -> dict:
        """Analyze user's weak skills based on quiz results"""
        results = self.db.query(Result).filter(Result.user_id == user_id).all()
        # TODO: Implement actual skill analysis logic
        return {
            "weak_skills": ["grammar", "vocabulary"],
            "strong_skills": ["reading"],
            "recommendation": "Focus on grammar and vocabulary exercises",
        }
