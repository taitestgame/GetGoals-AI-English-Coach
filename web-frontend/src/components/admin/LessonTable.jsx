import React from 'react';
const LessonTable = ({ lessons = [] }) => (
  <div className="lesson-table">
    <h3>Lessons Management</h3>
    <table>
      <thead><tr><th>ID</th><th>Title</th><th>Level</th><th>Category</th><th>Published</th><th>Actions</th></tr></thead>
      <tbody>{lessons.map(l => (
        <tr key={l.id}><td>{l.id}</td><td>{l.title}</td><td>{l.level}</td><td>{l.category}</td><td>{l.is_published ? 'Yes' : 'No'}</td><td><button>Edit</button><button>Delete</button></td></tr>
      ))}</tbody>
    </table>
  </div>
);
export default LessonTable;
