'''
Verkabelung von KY-023 (Joystick)
Joystick ...... ESP
GND             GND
+5V             3V3
VRx             D34
VRy             D35
SW              D32

Verkabelung des Servo
Servo ......... ESP
Braun           GND
Rot oder
Orange          VIN / 5V
Gelb (Signal)   D13

GPIOs für ADC Block 1: 32, 33, 34, 35, 36 und 39
GPIOs für ADC Block 2: 0, 2, 4, 12-15 und 25-27
'''

import machine
from machine import Pin, PWM
import time

# Joystick
joyX = machine.Pin(34, machine.Pin.IN)
joyY = machine.Pin(35, machine.Pin.IN)
joyButton = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

joyXadc = machine.ADC(joyX)
joyXadc.atten(machine.ADC.ATTN_11DB)
joyYadc = machine.ADC(joyY)
joyYadc.atten(machine.ADC.ATTN_11DB)

# Servo
servo1 = PWM(Pin(13), freq=50, duty=0)

def angle2duty(angle):
    # von 0 bis 180
    minDutyValue = 25
    maxDutyValue = 110    
    calculatedDutyValue = int(minDutyValue + ((angle/180) * (maxDutyValue-minDutyValue)))
    r = max(minDutyValue, min(calculatedDutyValue, maxDutyValue))
    print(r)
    return r

while True:
    valX = joyXadc.read()  #unsigned integer mit range 0-4095
    valY = joyYadc.read()  #unsigned integer mit range 0-4095
    position = valY / 22.75; # Divide up to 4095 by 22.5 int per °
    servo1.duty(angle2duty(position))
    print("Position: {position}".format(position=position)) # position in °
    time.sleep(0.5) #0.5 sekunden
