"""
User management routes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_active_user, get_admin_user
from app.models.user import User
from app.schemas.user_schema import UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_active_user)):
    """Get current user profile"""
    return current_user


@router.put("/me", response_model=UserResponse)
async def update_profile(
    user_data: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Update current user profile"""
    service = UserService(db)
    return service.update_user(current_user.id, user_data)


@router.get("/", response_model=list[UserResponse])
async def get_all_users(
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Get all users (admin only)"""
    service = UserService(db)
    return service.get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    """Get user by ID (admin only)"""
    service = UserService(db)
    return service.get_user_by_id(user_id)
