'''
Verkableung KY-040 (Rotary Encoder)
KY-040 ... ESP32
CLK        D13
DT         D14
SW         (nicht verbunden, SW ... switch ... ist der Button)
+          3V3
GND        GND
'''

import sys
import time
from rotary_irq_esp import RotaryIRQ

r = RotaryIRQ(pin_num_clk=13,
              pin_num_dt=14,
              min_val=0,
              max_val=5,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_WRAP)

val_old = r.value()
while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)

    time.sleep_ms(50)
