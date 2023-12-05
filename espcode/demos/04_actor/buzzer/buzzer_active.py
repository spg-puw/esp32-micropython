'''
Verbindungen
Buzzer active (KY-012) ... ESP
-                          GND
S                          D25
'''

'''
beim aktiven Buzzer kann die Frequenz NICHT verändert werden!
siehe: https://sensorkit.joy-it.net/de/sensors/ky-012
'''

import machine
import time

activeBuzzer = machine.Pin(25, machine.Pin.OUT)
time.sleep(1)

for t in range(1000, 0, -50):
    print("buzzing with t={}".format(t))
    activeBuzzer.value(1)
    time.sleep_ms(100)
    activeBuzzer.value(0)
    time.sleep_ms(t)

print("beeping")
for _ in range(40):
    activeBuzzer.value(1)
    time.sleep_ms(50)
    activeBuzzer.value(0)
    time.sleep_ms(50)
