import React from 'react';
const WeakSkillBox = ({ skills = [] }) => (
  <div className="weak-skill-box">
    <h3>Areas to Improve</h3>
    <div className="skill-tags">{skills.map((s, i) => <span key={i} className="skill-tag">{s}</span>)}</div>
  </div>
);
export default WeakSkillBox;
