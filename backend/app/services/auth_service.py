"""
Authentication service
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.auth_schema import LoginRequest, RegisterRequest, TokenResponse
from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token, decode_token


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register(self, request: RegisterRequest) -> TokenResponse:
        """Register a new user"""
        # Check if user already exists
        existing_user = self.db.query(User).filter(User.email == request.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        # Create new user
        user = User(
            email=request.email,
            full_name=request.full_name,
            hashed_password=get_password_hash(request.password),
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        # Generate tokens
        access_token = create_access_token(data={"sub": str(user.id)})
        refresh_token = create_refresh_token(data={"sub": str(user.id)})

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            user_id=user.id,
            full_name=user.full_name,
            role=user.role,
        )

    def login(self, request: LoginRequest) -> TokenResponse:
        """Login with email and password"""
        user = self.db.query(User).filter(User.email == request.email).first()
        if not user or not verify_password(request.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )

        access_token = create_access_token(data={"sub": str(user.id)})
        refresh_token = create_refresh_token(data={"sub": str(user.id)})

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            user_id=user.id,
            full_name=user.full_name,
            role=user.role,
        )

    def refresh(self, refresh_token: str) -> dict:
        """Refresh access token"""
        payload = decode_token(refresh_token)
        if not payload or payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )

        new_access_token = create_access_token(data={"sub": payload["sub"]})
        return {"access_token": new_access_token, "token_type": "bearer"}

    def google_login(self, id_token: str) -> TokenResponse:
        """Login with Google OAuth"""
        # TODO: Implement Google token verification
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Google login not yet implemented",
        )
