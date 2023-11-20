
from PCA9685 import PCA9685
import time
import numpy as np

Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

u,v = (0,0)


"""0 : gauche ; 1 : droite"""

monteurOn=True

class Motor_Driver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def Run(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                print ("1")
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                print ("2")
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                print ("3")
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                print ("4")
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def Stop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)


Motor = Motor_Driver()

while (monteurOn==True):

    if (v!=0):
        Theta=np.arctan((y/x))
    elif (v!=0):
        Theta=np.pi/2
    else :
        Theta=0

    if (u>= 0 and v>=0 ):

        Motor.Run(1, 'forward', (v**2+u**2)*((Theta*2)/(np.pi))*100)
        Motor.Run(0, 'forward', (v**2+u**2)*100)

    elif (u>0 and v<0):

        Motor.Run(0, 'forward', (v**2+u**2)*((abs(Theta*2)/(np.pi))*100)
        Motor.Run(1, 'forward', (v**2+u**2)*100)


    elif (u<0 and v<0):

        Motor.Run(0, 'backward', (v**2+u**2)*((Theta*2)/(np.pi))*100)
        Motor.Run(1, 'backward', (v**2+u**2)*100)

    else :

        Motor.Run(1, 'backward', (v**2+u**2)*((abs(Theta*2)/(np.pi))*100)
        Motor.Run(0, 'backward', (v**2+u**2)*100)



