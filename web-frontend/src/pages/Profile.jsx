import React from 'react';
import { useAuth } from '../hooks/useAuth';
const Profile = () => {
  const { user } = useAuth();
  return (<div className="profile-page"><h1>Profile</h1><div className="profile-info"><p><strong>Name:</strong> {user?.full_name}</p><p><strong>Email:</strong> {user?.email}</p></div></div>);
};
export default Profile;
