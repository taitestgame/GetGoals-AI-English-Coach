import React from 'react';
const UserTable = ({ users = [] }) => (
  <div className="user-table">
    <h3>Users Management</h3>
    <table>
      <thead><tr><th>ID</th><th>Name</th><th>Email</th><th>Role</th><th>Level</th><th>Actions</th></tr></thead>
      <tbody>{users.map(u => (
        <tr key={u.id}><td>{u.id}</td><td>{u.full_name}</td><td>{u.email}</td><td>{u.role}</td><td>{u.english_level || 'N/A'}</td><td><button>Edit</button></td></tr>
      ))}</tbody>
    </table>
  </div>
);
export default UserTable;
