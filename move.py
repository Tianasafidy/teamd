import asyncio
import websockets
import json
from PCA9685 import PCA9685
import time

Dir = [
    'forward',
    'backward',
]


pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

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

#server
connected = set()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                await conn.send(f'Got a new MSG FOR YOU: {message}')
                print(message)   
                
                try:
                    coord = json.loads(message)
                    coord_to_move(coord['x'], coord['y'], 100)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")



    except Exception as e:
        print(f"An execpiezjzked{type(e).__name__} occured: {e}")

    finally:
        # Unregister.
        connected.remove(websocket)
    
def coord_to_move(x,y,max = 100):
    if y > 0: #avancer
        if x <=0 : #gauche ou tout droit
            Motor.Run(0, 'forward', max) #Mot gauche 
            Motor.Run(1, 'forward', max + x) #Mot droite 

        else : #droite
            Motor.Run(0, 'forward', max) #Mot gauche 
            Motor.Run(1, 'forward', max - x) #Mot droite 
            
    elif y < 0: #reculer

        if x <= 0 :
            Motor.Run(0, 'forward', max) #Mot gauche 
            Motor.Run(1, 'forward', max + x) #Mot droite 

        else : #droite
            Motor.Run(0, 'forward', max) #Mot gauche 
            Motor.Run(1, 'forward', max - x) #Mot droite 
    
    else: #stop
        Motor.Stop(0)
        Motor.Stop(1)
    
start_server = websockets.serve(server, "localhost", 80)


asyncio.get_event_loop().run_until_complete(start_server)
print("running")
asyncio.get_event_loop().run_forever()






