'''
Verbindungen:
Servo (z.B. SG-5010) ... ESP32
Braun                    GND
Rot                      Vin / 5V
Orange                   Signal = Pin D13
'''

import machine
import time

servo1 = machine.PWM(machine.Pin(13), freq=50, duty=0)

def angle2duty(angle):
    # von 0 bis 180
    minDutyValue = 25+1
    maxDutyValue = 130-1 # for SG-5010
    maxDutyValue = 110 # little servo
    calculatedDutyValue = int(minDutyValue + ((angle/180) * (maxDutyValue-minDutyValue)))
    r = max(minDutyValue, min(calculatedDutyValue, maxDutyValue))
    print(r)
    return r

if __name__=="__main__":
    print("sweep")
    for i in range(180+1):
        servo1.duty(angle2duty(i))
        time.sleep(0.1)

    print("Positionen abfahren")
    for i in range(6):
        print("Position {i}".format(i=i))
        servo1.duty(angle2duty(i*36))
        time.sleep(2)
