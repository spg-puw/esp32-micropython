import time
from machine import Pin, ADC

# On the ESP32, ADC functionality is available on pins 32-39 (ADC block 1) and pins 0, 2, 4, 12-15 and 25-27 (ADC block 2).
# ADC block 2 is also used by WiFi and so attempting to read analog values from block 2 pins when WiFi is active will raise an exception.

# Note that the absolute maximum voltage rating for input pins is 3.6V. Going near to this boundary risks damage to the IC!

# ADC.ATTN_0DB: No attenuation (100mV - 950mV)
# ADC.ATTN_2_5DB: 2.5dB attenuation (100mV - 1250mV)
# ADC.ATTN_6DB: 6dB attenuation (150mV - 1750mV)
# ADC.ATTN_11DB: 11dB attenuation (150mV - 2450mV)

# supported ADC resolutions:
# ADC.WIDTH_9BIT = 9
# ADC.WIDTH_10BIT = 10
# ADC.WIDTH_11BIT = 11
# ADC.WIDTH_12BIT = 12

try:
    analogPin1 = ADC(Pin(32))
    analogPin1.atten(ADC.ATTN_11DB)
    while True:
        wert = analogPin1.read()
        print(wert)
        print("sleep 1s")
        time.sleep(1)
except:
    print("Abbruch!")