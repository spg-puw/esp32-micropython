'''
Verkablung für KY-052 - BMP280 (Temperatur und Luftdruck)
BMP280 ... ESP32
SDA        D21
SCL        D22
VCC        3V3
GND        GND
'''

import machine
import bmp280 # see lib/bmp280.py

i2c = machine.I2C(1, sda=machine.Pin(21), scl=machine.Pin(22))
bmp1 = bmp280.BMP280(i2c)

def cb_timer_bmp(t):
    print(str(bmp1.getTemp()) + ' C')
    print(str(bmp1.getPress()) + ' Pa')
    print(str(bmp1.getAltitude()) + ' m')
    print('----')

timer1 = machine.Timer(-1)
timer1.init(period=1000, mode=machine.Timer.PERIODIC, callback=cb_timer_bmp)
