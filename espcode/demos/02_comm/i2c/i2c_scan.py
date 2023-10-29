'''
Connect I2C device:
SDA ... D21
SCL ... D22

and start the scan to get device address(es)
'''

import machine

sdaPin=machine.Pin(21)
sclPin=machine.Pin(22)

i2c=machine.I2C(1, sda=sdaPin, scl=sclPin, freq=10000)

devices = i2c.scan()
if len(devices) == 0:
    print("no I2C device found")
else:
    print('i2c devices found:',len(devices))

for device in devices:
    print("   ... at address:",hex(device))
