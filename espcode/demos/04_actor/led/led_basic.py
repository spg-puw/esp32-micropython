'''
Verkabelung:
externe LED an Pin D13 anhängen und nicht auf Vorwiderstand (R >= 220 Ohm) vergessen

LED:
 - langes Bein ist + (Anode)
 - kurzes Bein ist - (Kathode)
'''

import machine
import time

ledIntern = machine.Pin(2, machine.Pin.OUT)
ledExtern = machine.Pin(13, machine.Pin.OUT) # Achtung: Vorwiderstand benutzen

print("interne LED blinkt")
ledIntern.on()
time.sleep(1)
ledIntern.off()
time.sleep(1)
ledIntern.value(1)
time.sleep(1)
ledIntern.value(0)
time.sleep(1)

print("externe LED blinkt")
ledExtern.on()
time.sleep(1)
ledExtern.off()
time.sleep(1)
ledExtern.value(1)
time.sleep(1)
ledExtern.value(0)
time.sleep(1)

print("Programm beendet")