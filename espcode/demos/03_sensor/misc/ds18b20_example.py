'''
Verkablung KY-001 - DS18B20 (Temperatursensor)
DS18B20 .......... ESP
-                  GND
+ (mittlerer Pin)  3V3
S                  D4
'''

import machine
import onewire
import ds18x20

ow = onewire.OneWire(machine.Pin(4))
dsSensor = ds18x20.DS18X20(ow)
memoryLocation = dsSensor.scan()

def timerCallback(t):
    dsSensor.convert_temp()
    temp = dsSensor.read_temp(memoryLocation[0])
    print("Temperatur: {0} °C".format(temp))

timer1 = machine.Timer(-1)
timer1.init(period=1000, mode=machine.Timer.PERIODIC, callback=timerCallback)
