'''
Verbindung mit dem Motorboard
Motorboard ... ESP32
IN1            D32
IN2            D33
IN3            D25
IN4            D26
- (bei 5-12V)  GND
+ (bei 5-12V)  Vin
'''

import machine
import time

# see lib/Stepper.py --> https://github.com/zhcong/ULN2003-for-ESP32/blob/master/Stepper.py
import Stepper

pinStepper1 = machine.Pin(32, machine.Pin.OUT)
pinStepper2 = machine.Pin(33, machine.Pin.OUT)
pinStepper3 = machine.Pin(25, machine.Pin.OUT)
pinStepper4 = machine.Pin(26, machine.Pin.OUT)

s1 = Stepper.create(pinStepper1, pinStepper2, pinStepper3, pinStepper4, delay=2)

numberSteps = 100
print("Legend:\n   CW ... clockwise\n   CCW ... counterclockwise")
print("make {0} steps CCW and then CW".format(numberSteps))
s1.step(numberSteps)
s1.step(numberSteps,-1) # or s1.step(-numberSteps)
print("make full rotation CCW and then CW")
s1.angle(360)
s1.angle(360,-1) # or s1.angle(-360)
