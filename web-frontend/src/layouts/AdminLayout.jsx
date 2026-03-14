import React from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from '../components/common/Navbar';

const AdminLayout = () => {
  return (
    <div className="admin-layout">
      <Navbar />
      <div className="admin-content">
        <aside className="admin-sidebar">
          <nav>
            <a href="/admin">Dashboard</a>
            <a href="/admin/users">Users</a>
            <a href="/admin/lessons">Lessons</a>
            <a href="/admin/quizzes">Quizzes</a>
          </nav>
        </aside>
        <main className="admin-main">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default AdminLayout;
