'''
Leuchtstreifen mit 15 Stk. WS2812B LEDs

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

anzahlLeds = 15
leuchtstreifenPin = machine.Pin(13, machine.Pin.OUT)
n = neopixel.NeoPixel(leuchtstreifenPin, anzahlLeds)

farbeRot = (255,0,0)
farbeGelb = (255,255,0)
farbeGruen = (0,255,0)
keineFarbe = (0,0,0) # die LED leuchtet NICHT

# initialzustand
for i in range(15):
    n[i] = keineFarbe
n.write() # Daten uebertragen

n[0] = farbeRot
n[1] = farbeGelb
n[2] = farbeGruen
n[13] = farbeRot
n[14] = farbeGruen
n.write()

time.sleep(2)

# nur die ersten 3 LEDs abschalten
n[0] = keineFarbe
n[1] = keineFarbe
n[2] = keineFarbe
n.write()

for _ in range(4): # gruen blinken
    n[2] = farbeGruen
    n.write()
    time.sleep(0.5)
    n[2] = keineFarbe
    n.write()
    time.sleep(0.5)
