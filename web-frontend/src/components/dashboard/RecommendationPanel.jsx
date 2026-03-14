import React from 'react';
const RecommendationPanel = ({ recommendations = [] }) => (
  <div className="recommendation-panel">
    <h3>AI Recommendations</h3>
    <ul>{recommendations.map((rec, i) => <li key={i}>{rec}</li>)}</ul>
  </div>
);
export default RecommendationPanel;
