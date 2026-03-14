"""
Response utilities
"""
from typing import Any, Optional


def success_response(data: Any = None, message: str = "Success"):
    return {"status": "success", "message": message, "data": data}


def error_response(message: str = "Error", status_code: int = 400):
    return {"status": "error", "message": message, "code": status_code}


def paginated_response(data: list, total: int, page: int = 1, page_size: int = 20):
    return {
        "status": "success",
        "data": data,
        "pagination": {
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size,
        },
    }
