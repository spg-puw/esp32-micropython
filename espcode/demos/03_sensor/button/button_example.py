'''
Verkabelung mit externem Button KY-004
Button ... ESP
-          GND
S          D13
'''

import machine
import time

ledIntern = machine.Pin(2, machine.Pin.OUT)
buttonBOOT = machine.Pin(0, machine.Pin.IN) # BOOT button on the ESP32 board
buttonExternal = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    print("Button BOOT: {0}\nButton extern: {1}".format(buttonBOOT.value(), buttonExternal.value()))
    ledIntern.value(not buttonBOOT.value())
    time.sleep(0.5)
    ledIntern.value(not buttonExternal.value())
    time.sleep(0.5)
