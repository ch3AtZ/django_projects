import React, { useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from '../AuthContext';

const Home = () => {
  const { token, logout } = useContext(AuthContext);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/home', {
          headers: { Authorization: `Bearer ${token}` },
        });
        console.log(response.data);
      } catch (err) {
        alert('Failed to fetch data');
      }
    };
    fetchData();
  }, [token]);

  return (
    <div>
      <h2>Welcome to the Home Page</h2>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default Home;
