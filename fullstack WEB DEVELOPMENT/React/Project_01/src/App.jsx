import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap';
import { Card } from 'react-bootstrap';
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
 import Header from './Components/Header';
 import Footer from './Components/Footer';
import Navbar from './Components/Navbar';

import Background from './Components/Background';
import Foreground from './Components/Foreground';

import axios from "axios";






function App() {
  
  return (
    <>
    <Background />
    <Foreground/>
    </>
    
    
  )
}

export default App;