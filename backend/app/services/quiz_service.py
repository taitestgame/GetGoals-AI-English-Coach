"""
Quiz service
"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.quiz import Quiz
from app.models.result import Result
from app.schemas.quiz_schema import QuizCreate, QuizSubmit


class QuizService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_quizzes(self):
        return self.db.query(Quiz).all()

    def get_quiz_by_id(self, quiz_id: int):
        quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
        return quiz

    def create_quiz(self, quiz_data: QuizCreate):
        quiz = Quiz(**quiz_data.model_dump())
        self.db.add(quiz)
        self.db.commit()
        self.db.refresh(quiz)
        return quiz

    def submit_quiz(self, quiz_id: int, user_id: int, submission: QuizSubmit):
        quiz = self.get_quiz_by_id(quiz_id)
        # Calculate score (simplified)
        total = len(quiz.questions) if quiz.questions else 0
        correct = 0  # TODO: Implement answer checking logic

        score = (correct / total * 100) if total > 0 else 0

        result = Result(
            user_id=user_id,
            quiz_id=quiz_id,
            score=score,
            total_questions=total,
            correct_answers=correct,
            answers=submission.answers,
            time_spent_seconds=submission.time_spent_seconds,
        )
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return {
            "quiz_id": quiz_id,
            "score": score,
            "total_questions": total,
            "correct_answers": correct,
            "feedback": "Good effort! Keep practicing." if score < 80 else "Excellent work!",
        }
