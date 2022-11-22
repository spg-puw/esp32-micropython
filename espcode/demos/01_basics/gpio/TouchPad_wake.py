import machine
import time
from machine import TouchPad, Pin
import esp32

print("start")

t = TouchPad(Pin(14))
t.config(500) # Schwellwert (threshold) einstellen

print("before wake") # Achtung: der Ausgabepuffer wird eventuell nicht vollständig geleert!
# time.sleep(0.1)

esp32.wake_on_touch(True)
machine.lightsleep()

print("after lightsleep")