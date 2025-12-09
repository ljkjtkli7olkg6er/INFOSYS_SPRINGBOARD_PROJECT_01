
import { Canvas } from '@react-three/fiber';
import './App.css';
import { OrbitControls } from '@react-three/drei';
import Cyl from "./Cyl"
import { useTexture } from '@react-three/drei';
import React from 'react';
import * as Three from 'three';

const App = () => {
   let img =useTexture('photo-collage.png.png');// Ensure the path is correct and the file is accessible
  
  return (
    <Canvas>  
      <OrbitControls />
      <ambientLight />
      
              <mesh>
                  <cylinderGeometry args={[1, 1, 1, 30, 30, true]} />
                  <meshStandardMaterial   side={Three.DoubleSide} color="grey" />
              </mesh>
    </Canvas>
  );
}

export default App;
