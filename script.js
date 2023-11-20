
const stick = document.querySelector('.stick');
const joystick = document.querySelector('.joystick');

let isDragging = false;

stick.addEventListener('mousedown', () => {
    isDragging = true;
});

const checkPoints = (x,y) => {
    return true;
};

document.addEventListener('mousemove', (e) => {
    if (isDragging) {
        const { top, left, width, height } = joystick.getBoundingClientRect();
        const { clientX, clientY } = e;
        const x = clientX - left - width / 2;
        const y = clientY - top - height / 2;
        const distance = Math.min(50, Math.sqrt(x * x + y * y));
       
       if((x<=100 && x>=-100) && (y<=100 && y>=-100)) {
         stick.style.transform = `translate(${x}px, ${y}px)`;
         console.log("x=",x);
         console.log("y=",y);
       }
        
    }
});



document.addEventListener('mouseup', () => {
    isDragging = false;
    stick.style.transform = 'translate(-50%, -50%)';
});
