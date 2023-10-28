'''
Verkablung MPU6050 (Beschleunigungssensor)
MPU6050 ... ESP32
VCC         3V3
GND         GND
SCL         D26
SDA         D25
'''

import machine
import time
import mpu6050

i2c = machine.SoftI2C(sda=machine.Pin(25), scl=machine.Pin(26))
accelerometer1 = mpu6050.accel(i2c)

print("Use the plotter in Thonny: View -> Plotter")

while True:
    print(accelerometer1.get_values())
    time.sleep_ms(100)
