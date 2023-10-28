'''
Verkabelung von KY-023 (Joystick)
Joystick ... ESP
GND          GND
+5V          3V3
VRx          D34
VRy          D35
SW           D32

GPIOs für ADC Block 1: 32, 33, 34, 35, 36 und 39
GPIOs für ADC Block 2: 0, 2, 4, 12-15 und 25-27
'''

import machine
import time

joyX = machine.Pin(34, machine.Pin.IN)
joyY = machine.Pin(35, machine.Pin.IN)
joyButton = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

joyXadc = machine.ADC(joyX)
joyXadc.atten(machine.ADC.ATTN_11DB)
joyYadc = machine.ADC(joyY)
joyYadc.atten(machine.ADC.ATTN_11DB)

while True:
    valX = joyXadc.read()  #unsigned integer mit range 0-4095
    valY = joyYadc.read()  #unsigned integer mit range 0-4095
    btn = not joyButton.value()
    print("X Wert: {x}      Y-Wert: {y}    Button: {b}".format(x=valX, y=valY, b=btn))
    time.sleep(0.5) #0.5 sekunden
