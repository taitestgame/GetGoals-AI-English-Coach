import React from 'react';
import { Link } from 'react-router-dom';
import Button from '../components/common/Button';

const Home = () => (
  <div className="home-page">
    <section className="hero">
      <h1>Welcome to GetGoals</h1>
      <p>Your AI-powered English learning coach. Personalized roadmaps, smart recommendations, and adaptive quizzes.</p>
      <div className="hero-actions">
        <Link to="/dashboard"><Button variant="primary">Go to Dashboard</Button></Link>
        <Link to="/lessons"><Button variant="secondary">Browse Lessons</Button></Link>
      </div>
    </section>
  </div>
);

export default Home;
