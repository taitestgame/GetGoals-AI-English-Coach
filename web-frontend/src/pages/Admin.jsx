import React from 'react';
import UserTable from '../components/admin/UserTable';
import LessonTable from '../components/admin/LessonTable';
import QuizManager from '../components/admin/QuizManager';

const Admin = () => (
  <div className="admin-page">
    <h1>Admin Panel</h1>
    <UserTable users={[]} />
    <LessonTable lessons={[]} />
    <QuizManager quizzes={[]} />
  </div>
);
export default Admin;
