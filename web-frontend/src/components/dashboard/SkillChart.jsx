import React from 'react';
const SkillChart = ({ skills = [] }) => (
  <div className="skill-chart">
    <h3>Skill Overview</h3>
    <div className="skills-list">
      {skills.map((skill) => (
        <div key={skill.name} className="skill-item">
          <span>{skill.name}</span>
          <div className="skill-bar"><div className="skill-fill" style={{ width: `${skill.score}%` }}></div></div>
          <span>{skill.score}%</span>
        </div>
      ))}
    </div>
  </div>
);
export default SkillChart;
