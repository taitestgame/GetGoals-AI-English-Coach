import React from 'react';
import AIResultCard from '../components/ai/AIResultCard';
import RoadmapCard from '../components/ai/RoadmapCard';
import WeakSkillBox from '../components/ai/WeakSkillBox';

const Roadmap = () => (
  <div className="roadmap-page">
    <h1>Learning Roadmap</h1>
    <AIResultCard result={{ predicted_level: 'B1', confidence: 0.75 }} />
    <WeakSkillBox skills={['grammar', 'listening']} />
    <RoadmapCard roadmap={{ title: 'B1 to B2 Path', description: 'Intermediate to Upper Intermediate', target_level: 'B2', estimated_days: 60 }} />
  </div>
);
export default Roadmap;
