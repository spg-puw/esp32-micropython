'''
Testskript für 100 Stk. WS2812B LEDs

Dokumentation: https://docs.micropython.org/en/latest/library/neopixel.html

Verkabelung:
Leuchstreifen ... ESP32
+5V .............. Vin
D0 ............... D13
GND .............. GND
'''

import machine
import time
import neopixel

anzahlLeds = 100
leuchtstreifenPin = machine.Pin(13, machine.Pin.OUT)
n = neopixel.NeoPixel(leuchtstreifenPin, anzahlLeds)

farbeRot = (255,0,0)

# initialzustand
for i in range(anzahlLeds):
    n[i] = farbeRot
n.write() # Daten uebertragen
