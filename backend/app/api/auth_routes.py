"""
Authentication routes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth_schema import LoginRequest, RegisterRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """Register a new user"""
    service = AuthService(db)
    return service.register(request)


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Login with email and password"""
    service = AuthService(db)
    return service.login(request)


@router.post("/refresh")
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    """Refresh access token"""
    service = AuthService(db)
    return service.refresh(refresh_token)


@router.post("/google")
async def google_login(id_token: str, db: Session = Depends(get_db)):
    """Login with Google OAuth"""
    service = AuthService(db)
    return service.google_login(id_token)
