const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById("container").appendChild(renderer.domElement);

function updateNodes(fusionScore) {

    nodes.forEach(n => {
        n.scale.setScalar(1 + fusionScore * 0.1);
    });
}


// Earth
const geometry = new THREE.SphereGeometry(5, 64, 64);
const material = new THREE.MeshBasicMaterial({ wireframe: true });
const earth = new THREE.Mesh(geometry, material);
scene.add(earth);

camera.position.z = 10;

// Node positions (simplified)
const nodes = [];

function addNode(lat, lon, color=0x00ffcc) {
    const phi = (90 - lat) * Math.PI/180;
    const theta = (lon + 180) * Math.PI/180;

    const x = -5 * Math.sin(phi) * Math.cos(theta);
    const y =  5 * Math.cos(phi);
    const z =  5 * Math.sin(phi) * Math.sin(theta);

    const sphere = new THREE.Mesh(
        new THREE.SphereGeometry(0.15),
        new THREE.MeshBasicMaterial({ color })
    );

    sphere.position.set(x,y,z);
    scene.add(sphere);
    nodes.push(sphere);
}

// Example nodes (expand freely)
addNode(52.52, 13.40); // Berlin
addNode(48.13, 11.58); // Munich
addNode(50.94, 6.96);  // Cologne
addNode(40.71, -74.00); // NYC

function animate() {
    requestAnimationFrame(animate);

    earth.rotation.y += 0.002;

    // pulse nodes
    nodes.forEach(n => {
        n.scale.setScalar(1 + Math.sin(Date.now()*0.005)*0.3);
    });

    renderer.render(scene, camera);
}

animate();