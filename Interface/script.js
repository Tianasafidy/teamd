// Crée WebSocket connection.
const socket = new WebSocket('ws://localhost:80');

const stick = document.querySelector('.stick');
const stickOverlay = document.querySelector('.stickOverlay');
const joystick = document.querySelector('.joystick');
let isDragging = false;

// Connection opened
socket.addEventListener('open', function (event) {
    console.log('Connected to the WS Server!');
});

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
});

const sendMsg = (x, y) => {
    const data = {
        x: x,
        y: y,
    };
    const jsonData = JSON.stringify(data);
    socket.send(jsonData);
};

stickOverlay.addEventListener('mousedown', () => {
    isDragging = true;
});

stickOverlay.addEventListener('touchstart', (e) => {
    e.preventDefault(); // Prevent default touch event behavior
    isDragging = true;
});

const checkPoints = (x, y) => {
    return true;
};

const handleMove = (event) => {
   
    if (isDragging) {

    
        const { top, left, width, height } = joystick.getBoundingClientRect();
        const clientX = event.touches ? event.touches[0].clientX : event.clientX;
        const clientY = event.touches ? event.touches[0].clientY : event.clientY;
        const x = clientX - left - width / 2;
        const y = clientY - top - height / 2;
        const distance = Math.sqrt(x * x + y * y);

        const maxDistance = width / 2 - stick.offsetWidth / 2;

        if (distance <= maxDistance) {
            stick.style.transform = `translate(${x}px, ${y}px)`;
            sendMsg(x, -y);
        } else {
            const clampedX = (x / distance) * maxDistance;
            const clampedY = (y / distance) * maxDistance;
            stick.style.transform = `translate(${clampedX}px, ${clampedY}px)`;
        
    }
}
};

document.addEventListener('mousemove', handleMove);
document.addEventListener('touchmove', handleMove);

document.addEventListener('mouseup', () => {
    isDragging = false;
    stick.style.transform = 'translate(-50%, -50%)';
});

document.addEventListener('touchend', () => {
    isDragging = false;
    stick.style.transform = 'translate(-50%, -50%)';
});



//  // Create WebSocket connection.
//  const socket = new WebSocket('ws://localhost:80');

//  const stick = document.querySelector('.stick');
//  const stickOverlay = document.querySelector('.stickOverlay');
//  const joystick = document.querySelector('.joystick');
//  let isDragging = false;

//  // Connection opened
//  socket.addEventListener('open', function (event) {
//      console.log('Connected to the WS Server!')
//  });

//  // Listen for messages
//  socket.addEventListener('message', function (event) {
//      console.log('Message from server ', event.data);
//  });

//  const sendMsg = (x, y) => {
//     // Crée un objet JSON avec les valeurs de x et y
//     const data = {
//         x: x,
//         y: y,
//     };
//     // Convertit l'objet data en une chaîne JSON
//     const jsonData = JSON.stringify(data);

//     // Envoie la chaîne JSON via le WebSocket
//     socket.send(jsonData);
// }

// stickOverlay.addEventListener('mousedown', () => {
//     isDragging = true;
// });

// const checkPoints = (x,y) => {
//     return true;
// };

// document.addEventListener('mousemove', (e) => {
//     if (isDragging) {
//         const { top, left, width, height } = joystick.getBoundingClientRect();
//         const { clientX, clientY } = e;
//         const x = clientX - left - width / 2;
//         const y = clientY - top - height / 2;
//         const distance = Math.sqrt(x * x + y * y);

//         // Define the maximum allowable distance from the center
//         const maxDistance = width / 2 - stick.offsetWidth / 2;

//         // Ensure the stick stays within the defined boundary
//         if (distance <= maxDistance) {
//             stick.style.transform = `translate(${x}px, ${y}px)`;
//             console.log("x=", x);
//             console.log("y=", y);
//             sendMsg(x, -y);;
//         } else {
//             // Calculate the clamped position within the boundary
//             const clampedX = (x / distance) * maxDistance;
//             const clampedY = (y / distance) * maxDistance;

//             stick.style.transform = `translate(${clampedX}px, ${clampedY}px)`;
//         }
//     }
// });

// document.addEventListener('mouseup', () => {
//     isDragging = false;
//      stick.style.transform = 'translate(-50%, -50%)';
// });
