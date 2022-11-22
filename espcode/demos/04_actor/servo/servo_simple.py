from machine import Pin, PWM
import time

servo1 = PWM(Pin(18), freq=50, duty=0)

def Servo(servo,angle):
    servo1.duty(int(((angle+90)*2/180+0.5)/20*1023))

Servo(servo1,-90)
time.sleep(1)

Servo(servo1,-45)
time.sleep(1)

Servo(servo1,0)
time.sleep(1)

Servo(servo1,45)
time.sleep(1)

Servo(servo1,90)
time.sleep(1)