'''
Pico Relay B (8ch, see: https://www.waveshare.com/pico-relay-b.htm)
Verwenden mit Raspberry Pi pico
'''

import machine
import neopixel
import time

ch1 = machine.Pin(21, machine.Pin.OUT)
ch2 = machine.Pin(20, machine.Pin.OUT)
ch3 = machine.Pin(19, machine.Pin.OUT)
ch4 = machine.Pin(18, machine.Pin.OUT)
ch5 = machine.Pin(17, machine.Pin.OUT)
ch6 = machine.Pin(16, machine.Pin.OUT)
ch7 = machine.Pin(15, machine.Pin.OUT)
ch8 = machine.Pin(14, machine.Pin.OUT)

buzzer = machine.Pin(6, machine.Pin.OUT)
rgbLed = machine.Pin(13, machine.Pin.OUT)
n = neopixel.NeoPixel(rgbLed, 1)

farbeRot = (255,0,0)
farbeGelb = (255,255,0)
farbeGruen = (0,255,0)
keineFarbe = (0,0,0)

print("Farben zeigen")
for farbe in [farbeRot, farbeGelb, farbeGruen, keineFarbe]:
    n[0] = farbe
    n.write()
    time.sleep(1)
    
print("Relays ein/aus")
for ch in [ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8]:
    ch.on()
    time.sleep(1)
    ch.off()
    time.sleep(1)
