"""
Roadmap management routes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.models.user import User
from app.services.roadmap_service import RoadmapService

router = APIRouter()


@router.get("/")
async def get_roadmaps(db: Session = Depends(get_db)):
    """Get all available roadmaps"""
    service = RoadmapService(db)
    return service.get_all_roadmaps()


@router.get("/my")
async def get_my_roadmap(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Get current user's active roadmap"""
    service = RoadmapService(db)
    return service.get_user_roadmap(current_user.id)


@router.post("/{roadmap_id}/enroll")
async def enroll_roadmap(
    roadmap_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Enroll in a roadmap"""
    service = RoadmapService(db)
    return service.enroll_user(current_user.id, roadmap_id)


@router.put("/{roadmap_id}/progress")
async def update_progress(
    roadmap_id: int,
    progress: dict,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Update roadmap progress"""
    service = RoadmapService(db)
    return service.update_progress(current_user.id, roadmap_id, progress)
