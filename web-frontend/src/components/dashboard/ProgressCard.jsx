import React from 'react';
const ProgressCard = ({ title, value, max, unit = '%' }) => (
  <div className="progress-card">
    <h3>{title}</h3>
    <div className="progress-bar"><div className="progress-fill" style={{ width: `${(value / max) * 100}%` }}></div></div>
    <p>{value}{unit} / {max}{unit}</p>
  </div>
);
export default ProgressCard;
