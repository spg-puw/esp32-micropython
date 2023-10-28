'''
Verkablung KY-015 - DHT11 Temperatur und Luftfeuchte
DHT11 ............ ESP
-                  GND
+ (mittlerer Pin)  3V3
S                  D27
'''

import machine
import time
import dht

d = dht.DHT11(machine.Pin(27))
time.sleep(1)

def dhtCallback(t):
    d.measure()
    print("Messergebnis: {0} °C mit {1} % Luftfeuchte".format(d.temperature(), d.humidity()))

timer1 = machine.Timer(-1)
timer1.init(period=2000, mode=machine.Timer.PERIODIC, callback=dhtCallback)

print("Auf den Sensor hauchen, damit sich die Werte verändern!")
