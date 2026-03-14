# API Documentation

## Base URL
```
http://localhost:8000/api
```

## Authentication

### POST /auth/register
Register a new user.

### POST /auth/login
Login with email and password.

### POST /auth/refresh
Refresh access token.

### POST /auth/google
Login with Google OAuth.

## Users

### GET /users/me
Get current user profile. (Auth required)

### PUT /users/me
Update current user profile. (Auth required)

### GET /users/
Get all users. (Admin only)

## Lessons

### GET /lessons/
Get all lessons.

### GET /lessons/{id}
Get a specific lesson.

### POST /lessons/
Create a lesson. (Admin only)

### PUT /lessons/{id}
Update a lesson. (Admin only)

### DELETE /lessons/{id}
Delete a lesson. (Admin only)

## Quizzes

### GET /quizzes/
Get all quizzes.

### GET /quizzes/{id}
Get a specific quiz.

### POST /quizzes/
Create a quiz. (Admin only)

### POST /quizzes/{id}/submit
Submit quiz answers. (Auth required)

## Results

### GET /results/
Get current user's results. (Auth required)

### GET /results/{id}
Get a specific result. (Auth required)

### GET /results/summary/me
Get result summary. (Auth required)

## AI

### POST /ai/predict-level
Predict English level. (Auth required)

### GET /ai/recommendation
Get AI roadmap recommendation. (Auth required)

### GET /ai/weak-skills
Get weak skills analysis. (Auth required)

## Roadmaps

### GET /roadmaps/
Get all roadmaps.

### GET /roadmaps/my
Get current user's roadmap. (Auth required)

### POST /roadmaps/{id}/enroll
Enroll in a roadmap. (Auth required)

### PUT /roadmaps/{id}/progress
Update roadmap progress. (Auth required)
