import React from 'react';
const AIResultCard = ({ result }) => (
  <div className="ai-result-card">
    <h3>AI Analysis Result</h3>
    <p>Predicted Level: <strong>{result?.predicted_level || 'N/A'}</strong></p>
    <p>Confidence: <strong>{result?.confidence ? `${(result.confidence * 100).toFixed(1)}%` : 'N/A'}</strong></p>
  </div>
);
export default AIResultCard;
