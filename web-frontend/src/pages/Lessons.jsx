import React, { useEffect, useState } from 'react';
import { lessonService } from '../services/lessonService';

const Lessons = () => {
  const [lessons, setLessons] = useState([]);

  useEffect(() => {
    lessonService.getAll().then(setLessons).catch(console.error);
  }, []);

  return (
    <div className="lessons-page">
      <h1>Lessons</h1>
      <div className="lessons-grid">
        {lessons.map(lesson => (
          <div key={lesson.id} className="lesson-card">
            <h3>{lesson.title}</h3>
            <span className="level-badge">{lesson.level}</span>
            <p>{lesson.description}</p>
            <p>{lesson.duration_minutes} min</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Lessons;
