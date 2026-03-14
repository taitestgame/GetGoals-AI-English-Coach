import React, { useEffect, useState } from 'react';
import { resultService } from '../services/resultService';

const Results = () => {
  const [results, setResults] = useState([]);
  useEffect(() => { resultService.getMyResults().then(setResults).catch(console.error); }, []);
  return (
    <div className="results-page"><h1>My Results</h1>
      <div className="results-list">{results.map(r => (
        <div key={r.id} className="result-card"><p>Quiz #{r.quiz_id}</p><p>Score: {r.score}%</p><p>Correct: {r.correct_answers}/{r.total_questions}</p></div>
      ))}</div>
    </div>
  );
};
export default Results;
