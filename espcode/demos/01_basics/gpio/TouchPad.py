import machine
import time

touchPin1 = machine.TouchPad(machine.Pin(14))

gelesenerWert = 0

while True:
    gelesenerWert = touchPin1.read()
    print(gelesenerWert)

    time.sleep(0.1)