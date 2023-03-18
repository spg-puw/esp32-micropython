from machine import Pin, PWM
import time

# Verbindungen Servo
# Braun = GND
# Rot = Vin / 5V
# Orange = Signal = Pin D13
servo1 = PWM(Pin(13), freq=50, duty=0)

def angle2duty(angle):
    # von 0 bis 180
    minDutyValue = 102
    maxDutyValue = 204    
    calculatedDutyValue = int(minDutyValue + ((angle/180) * (maxDutyValue-minDutyValue)))
    r = max(minDutyValue, min(calculatedDutyValue, maxDutyValue))
    print(r)
    return r

for i in range(6):
    print("Position {i}".format(i=i))
    servo1.duty(angle2duty(i*36))
    time.sleep(1)
