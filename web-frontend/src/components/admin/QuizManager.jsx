import React from 'react';
const QuizManager = ({ quizzes = [] }) => (
  <div className="quiz-manager">
    <h3>Quiz Management</h3>
    <button className="btn btn-primary">Create Quiz</button>
    <table>
      <thead><tr><th>ID</th><th>Title</th><th>Level</th><th>Type</th><th>Actions</th></tr></thead>
      <tbody>{quizzes.map(q => (
        <tr key={q.id}><td>{q.id}</td><td>{q.title}</td><td>{q.level}</td><td>{q.quiz_type}</td><td><button>Edit</button><button>Delete</button></td></tr>
      ))}</tbody>
    </table>
  </div>
);
export default QuizManager;
