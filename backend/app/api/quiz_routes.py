"""
Quiz management routes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_active_user, get_admin_user
from app.models.user import User
from app.schemas.quiz_schema import QuizCreate, QuizResponse, QuizSubmit, QuizResultResponse
from app.services.quiz_service import QuizService

router = APIRouter()


@router.get("/", response_model=list[QuizResponse])
async def get_quizzes(db: Session = Depends(get_db)):
    """Get all quizzes"""
    service = QuizService(db)
    return service.get_all_quizzes()


@router.get("/{quiz_id}", response_model=QuizResponse)
async def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    """Get a specific quiz"""
    service = QuizService(db)
    return service.get_quiz_by_id(quiz_id)


@router.post("/", response_model=QuizResponse)
async def create_quiz(
    quiz: QuizCreate,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Create a new quiz (admin only)"""
    service = QuizService(db)
    return service.create_quiz(quiz)


@router.post("/{quiz_id}/submit", response_model=QuizResultResponse)
async def submit_quiz(
    quiz_id: int,
    submission: QuizSubmit,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Submit quiz answers"""
    service = QuizService(db)
    return service.submit_quiz(quiz_id, current_user.id, submission)
