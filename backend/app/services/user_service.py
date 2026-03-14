"""
User service
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user_schema import UserUpdate


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        """Get all users"""
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        """Get user by ID"""
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def update_user(self, user_id: int, user_data: UserUpdate):
        """Update user profile"""
        user = self.get_user_by_id(user_id)
        update_data = user_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user
