'''
Verkabelung KY-050 (Ultraschall-Abstandssensor)
KY-050 ... ESP32
Vcc        Vin
Trig       D18
Echo       D19
Gnd        GND

Anmerkung: bitte 5V (Vin-Pin bei USB) verwenden!
'''
from hcsr04 import HCSR04 # see lib/hcsr04.py
import time

sensor = HCSR04(trigger_pin=18, echo_pin=19)

print("Use the plotter in Thonny: View -> Plotter")

while True:
    d = sensor.distance_cm()
    print(d)
    time.sleep(0.1)
