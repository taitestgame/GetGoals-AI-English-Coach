"""
Lesson repository
"""
from sqlalchemy.orm import Session
from app.models.lesson import Lesson


class LessonRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, lesson_id: int):
        return self.db.query(Lesson).filter(Lesson.id == lesson_id).first()

    def get_all(self):
        return self.db.query(Lesson).order_by(Lesson.order_index).all()

    def get_by_level(self, level: str):
        return self.db.query(Lesson).filter(Lesson.level == level).all()

    def create(self, lesson: Lesson):
        self.db.add(lesson)
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def update(self, lesson: Lesson):
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def delete(self, lesson_id: int):
        lesson = self.get_by_id(lesson_id)
        if lesson:
            self.db.delete(lesson)
            self.db.commit()
