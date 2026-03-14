"""
Validation utilities
"""
import re
from fastapi import HTTPException


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_password(password: str) -> bool:
    """Validate password strength"""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True


def validate_english_level(level: str) -> bool:
    """Validate English level"""
    valid_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    return level in valid_levels
