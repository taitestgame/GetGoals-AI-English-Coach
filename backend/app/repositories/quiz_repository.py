"""
Quiz repository
"""
from sqlalchemy.orm import Session
from app.models.quiz import Quiz


class QuizRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, quiz_id: int):
        return self.db.query(Quiz).filter(Quiz.id == quiz_id).first()

    def get_all(self):
        return self.db.query(Quiz).all()

    def get_by_lesson(self, lesson_id: int):
        return self.db.query(Quiz).filter(Quiz.lesson_id == lesson_id).all()

    def get_by_level(self, level: str):
        return self.db.query(Quiz).filter(Quiz.level == level).all()

    def create(self, quiz: Quiz):
        self.db.add(quiz)
        self.db.commit()
        self.db.refresh(quiz)
        return quiz

    def delete(self, quiz_id: int):
        quiz = self.get_by_id(quiz_id)
        if quiz:
            self.db.delete(quiz)
            self.db.commit()
