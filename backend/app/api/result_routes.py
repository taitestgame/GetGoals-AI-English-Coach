"""
Result management routes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.models.user import User
from app.schemas.result_schema import ResultResponse
from app.services.result_service import ResultService

router = APIRouter()


@router.get("/", response_model=list[ResultResponse])
async def get_my_results(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Get current user's results"""
    service = ResultService(db)
    return service.get_user_results(current_user.id)


@router.get("/{result_id}", response_model=ResultResponse)
async def get_result(
    result_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Get a specific result"""
    service = ResultService(db)
    return service.get_result_by_id(result_id, current_user.id)


@router.get("/summary/me")
async def get_my_summary(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Get current user's result summary"""
    service = ResultService(db)
    return service.get_user_summary(current_user.id)
