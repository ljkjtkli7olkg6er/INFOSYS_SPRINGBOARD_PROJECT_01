import { useTexture } from '@react-three/drei';
import React from 'react';
import * as Three from 'three';

const Cyl = () => {
    const tex = useTexture(); // Ensure the path is correct and the file is accessible

    return (
        <mesh>
            <cylinderGeometry args={[1, 1, 1, 30, 30, true]} />
            <meshStandardMaterial  transparent side={Three.DoubleSide} color="grey" />
        </mesh>
    );
}

export default Cyl;
