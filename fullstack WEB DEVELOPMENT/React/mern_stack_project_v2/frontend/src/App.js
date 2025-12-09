import React, { useContext } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Home from './pages/Home';
import { AuthContext, AuthProvider } from './context/AuthContext';

function App() {
  const { user } = useContext(AuthContext);
  return (
    <AuthProvider>
      {user ? <Home /> : <><Login /> <Register /></>}
    </AuthProvider>
  );
}

export default App;