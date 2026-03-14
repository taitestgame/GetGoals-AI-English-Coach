import React from 'react';
const RoadmapCard = ({ roadmap }) => (
  <div className="roadmap-card">
    <h3>{roadmap?.title || 'Learning Roadmap'}</h3>
    <p>{roadmap?.description}</p>
    <p>Target: {roadmap?.target_level} | Est. {roadmap?.estimated_days} days</p>
  </div>
);
export default RoadmapCard;
