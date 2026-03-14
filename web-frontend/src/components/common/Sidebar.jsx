import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <nav>
        <Link to="/dashboard">📊 Dashboard</Link>
        <Link to="/lessons">📚 Lessons</Link>
        <Link to="/quiz">✍️ Quiz</Link>
        <Link to="/results">📈 Results</Link>
        <Link to="/roadmap">🗺️ Roadmap</Link>
        <Link to="/profile">👤 Profile</Link>
      </nav>
    </aside>
  );
};

export default Sidebar;
