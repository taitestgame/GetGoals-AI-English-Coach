import React from 'react';
import ProgressCard from '../components/dashboard/ProgressCard';
import SkillChart from '../components/dashboard/SkillChart';
import RecommendationPanel from '../components/dashboard/RecommendationPanel';

const Dashboard = () => (
  <div className="dashboard-page">
    <h1>Dashboard</h1>
    <div className="dashboard-grid">
      <ProgressCard title="Overall Progress" value={65} max={100} />
      <ProgressCard title="Lessons Completed" value={12} max={20} />
      <ProgressCard title="Quizzes Taken" value={8} max={15} />
    </div>
    <SkillChart skills={[
      { name: 'Grammar', score: 75 },
      { name: 'Vocabulary', score: 60 },
      { name: 'Reading', score: 80 },
      { name: 'Listening', score: 55 },
      { name: 'Speaking', score: 45 },
      { name: 'Writing', score: 65 },
    ]} />
    <RecommendationPanel recommendations={['Focus on speaking practice', 'Review grammar rules', 'Try listening exercises']} />
  </div>
);

export default Dashboard;
