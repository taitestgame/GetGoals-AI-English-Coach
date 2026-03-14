"""
Lesson management routes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_active_user, get_admin_user
from app.models.user import User
from app.schemas.lesson_schema import LessonCreate, LessonResponse, LessonUpdate
from app.services.lesson_service import LessonService

router = APIRouter()


@router.get("/", response_model=list[LessonResponse])
async def get_lessons(db: Session = Depends(get_db)):
    """Get all lessons"""
    service = LessonService(db)
    return service.get_all_lessons()


@router.get("/{lesson_id}", response_model=LessonResponse)
async def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    """Get a specific lesson"""
    service = LessonService(db)
    return service.get_lesson_by_id(lesson_id)


@router.post("/", response_model=LessonResponse)
async def create_lesson(
    lesson: LessonCreate,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Create a new lesson (admin only)"""
    service = LessonService(db)
    return service.create_lesson(lesson)


@router.put("/{lesson_id}", response_model=LessonResponse)
async def update_lesson(
    lesson_id: int,
    lesson: LessonUpdate,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Update a lesson (admin only)"""
    service = LessonService(db)
    return service.update_lesson(lesson_id, lesson)


@router.delete("/{lesson_id}")
async def delete_lesson(
    lesson_id: int,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Delete a lesson (admin only)"""
    service = LessonService(db)
    return service.delete_lesson(lesson_id)
