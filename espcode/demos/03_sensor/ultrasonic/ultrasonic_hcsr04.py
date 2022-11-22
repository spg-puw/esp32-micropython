from hcsr04 import HCSR04
import time

# bitte 5V (VIN-Pin bei USB) verwenden!

sensor = HCSR04(trigger_pin=18, echo_pin=19)
while True:
    d = sensor.distance_cm()
    print(d)
    time.sleep(0.1)