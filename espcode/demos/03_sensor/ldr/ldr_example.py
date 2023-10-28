'''
Verkablung KY-018 - LDR (Fotowiderstand)
LDR .............. ESP32
S                  D32
+ (mittlerer Pin)  Vin (als Alternative auch 3V3)
-                  GND
'''

import machine

ldr1 = machine.ADC(machine.Pin(32))
ldr1.atten(machine.ADC.ATTN_11DB)

def timerCallback(t):
    value = ldr1.read()
    print("\nMesswert = {0} --> {1:.2f} V".format(value, value/4095*3.3))

    if 0 <= value <=1500:
        print("  `-> stark")
    elif 1500 < value <= 2800:
        print("  `-> normal")
    elif 2800 < value <= 4095:
        print("  `-> schwach")

timer1 = machine.Timer(-1)
timer1.init(period=1000, mode=machine.Timer.PERIODIC, callback=timerCallback)
