"""
Result repository
"""
from sqlalchemy.orm import Session
from app.models.result import Result


class ResultRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, result_id: int):
        return self.db.query(Result).filter(Result.id == result_id).first()

    def get_by_user(self, user_id: int):
        return self.db.query(Result).filter(Result.user_id == user_id).all()

    def get_by_quiz(self, quiz_id: int):
        return self.db.query(Result).filter(Result.quiz_id == quiz_id).all()

    def create(self, result: Result):
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        return result
