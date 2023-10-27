import machine
import time
import esp32

print("start, please touch pin D14")

touchPin = machine.TouchPad(machine.Pin(14))
touchPin.config(500) # Schwellwert (threshold) einstellen

print("before wake") # Achtung: der Ausgabepuffer wird eventuell nicht vollständig geleert!
# time.sleep(0.1) # kurz warten, damit der Ausgabepuffer geleert wird

esp32.wake_on_touch(True)
machine.lightsleep()

print("after lightsleep")