"""
User schemas
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: str
    full_name: str


class UserResponse(UserBase):
    id: int
    avatar_url: Optional[str] = None
    role: str
    is_active: bool
    english_level: Optional[str] = None
    auth_provider: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    english_level: Optional[str] = None
