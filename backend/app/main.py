"""
GetGoals AI English Coach - Backend API
Main entry point for FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import (
    auth_routes,
    user_routes,
    lesson_routes,
    quiz_routes,
    result_routes,
    ai_routes,
    roadmap_routes,
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="GetGoals AI English Coach API",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])
app.include_router(lesson_routes.router, prefix="/api/lessons", tags=["Lessons"])
app.include_router(quiz_routes.router, prefix="/api/quizzes", tags=["Quizzes"])
app.include_router(result_routes.router, prefix="/api/results", tags=["Results"])
app.include_router(ai_routes.router, prefix="/api/ai", tags=["AI"])
app.include_router(roadmap_routes.router, prefix="/api/roadmaps", tags=["Roadmaps"])


@app.get("/")
async def root():
    return {"message": "Welcome to GetGoals AI English Coach API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
