"""
Result service
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.result import Result


class ResultService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_results(self, user_id: int):
        return self.db.query(Result).filter(Result.user_id == user_id).all()

    def get_result_by_id(self, result_id: int, user_id: int):
        result = self.db.query(Result).filter(
            Result.id == result_id, Result.user_id == user_id
        ).first()
        if not result:
            raise HTTPException(status_code=404, detail="Result not found")
        return result

    def get_user_summary(self, user_id: int):
        results = self.get_user_results(user_id)
        if not results:
            return {"total_quizzes": 0, "average_score": 0, "best_score": 0}

        scores = [r.score for r in results]
        return {
            "total_quizzes": len(results),
            "average_score": round(sum(scores) / len(scores), 2),
            "best_score": max(scores),
            "latest_score": scores[-1],
        }
