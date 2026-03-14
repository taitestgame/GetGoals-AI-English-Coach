"""
Helper utilities
"""
from datetime import datetime


def format_datetime(dt: datetime) -> str:
    """Format datetime to string"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def calculate_percentage(part: int, total: int) -> float:
    """Calculate percentage"""
    if total == 0:
        return 0.0
    return round((part / total) * 100, 2)


def generate_feedback(score: float) -> str:
    """Generate feedback based on score"""
    if score >= 90:
        return "Excellent! You're doing great!"
    elif score >= 70:
        return "Good job! Keep up the great work!"
    elif score >= 50:
        return "Not bad! There's room for improvement."
    else:
        return "Keep practicing! You'll get better with time."
