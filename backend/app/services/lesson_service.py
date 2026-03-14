"""
Lesson service
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.lesson import Lesson
from app.schemas.lesson_schema import LessonCreate, LessonUpdate


class LessonService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_lessons(self):
        return self.db.query(Lesson).order_by(Lesson.order_index).all()

    def get_lesson_by_id(self, lesson_id: int):
        lesson = self.db.query(Lesson).filter(Lesson.id == lesson_id).first()
        if not lesson:
            raise HTTPException(status_code=404, detail="Lesson not found")
        return lesson

    def create_lesson(self, lesson_data: LessonCreate):
        lesson = Lesson(**lesson_data.model_dump())
        self.db.add(lesson)
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def update_lesson(self, lesson_id: int, lesson_data: LessonUpdate):
        lesson = self.get_lesson_by_id(lesson_id)
        update_data = lesson_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(lesson, key, value)
        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def delete_lesson(self, lesson_id: int):
        lesson = self.get_lesson_by_id(lesson_id)
        self.db.delete(lesson)
        self.db.commit()
        return {"message": "Lesson deleted successfully"}
