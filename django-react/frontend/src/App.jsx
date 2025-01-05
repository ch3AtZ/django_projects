import { useState } from 'react'
import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'

//
import Login from './pages/Login'
import Register from './pages/Register'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoute'

// Utility function to handle logout
const Logout = () => {
  localStorage.clear()
  return <Navigate to="/login" replace />
}

// Handle registration with proper cleanup
const RegisterAndLogout = () => {
  React.useEffect(() => {
    localStorage.clear()
  }, [])
  
  return <Register />
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        } />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App