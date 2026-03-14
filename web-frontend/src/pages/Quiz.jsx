import React, { useEffect, useState } from 'react';
import { quizService } from '../services/quizService';

const Quiz = () => {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    quizService.getAll().then(setQuizzes).catch(console.error);
  }, []);

  return (
    <div className="quiz-page">
      <h1>Quizzes</h1>
      <div className="quiz-grid">
        {quizzes.map(quiz => (
          <div key={quiz.id} className="quiz-card">
            <h3>{quiz.title}</h3>
            <span className="level-badge">{quiz.level}</span>
            <p>{quiz.quiz_type} | {quiz.time_limit_minutes} min</p>
            <button className="btn btn-primary">Start Quiz</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Quiz;
