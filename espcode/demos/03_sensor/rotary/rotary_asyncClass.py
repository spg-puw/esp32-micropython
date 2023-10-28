'''
Es werden 2 Stk. KY-040 benötigt!

Verkableung KY-040 (Rotary Encoder)
Encoder 1 ... ESP32
CLK           D13
DT            D14
SW            (nicht verbunden, SW ... switch ... ist der Button)
+             3V3
GND           GND

Encoder 2 ... ESP32
CLK           D18
DT            D19
SW            (nicht verbunden, SW ... switch ... ist der Button)
+             3V3
GND           GND
'''

# example for MicroPython rotary encoder
# - uasyncio implementation
# - 2 independent rotary encoders
# - register callbacks with the rotary objects
# - shows the use of an Observer pattern in Python

import sys
from rotary_irq_esp import RotaryIRQ
import uasyncio as asyncio

# example of a class that uses one rotary encoder
class Application1():
    def __init__(self, r1):
        self.r1 = r1
        self.myevent = asyncio.Event()
        asyncio.create_task(self.action())
        r1.add_listener(self.callback)

    def callback(self):
        self.myevent.set()

    async def action(self):
        while True:
            await self.myevent.wait()
            print('App 1:  rotary 1 = {}'. format(self.r1.value()))
            # do something with the encoder result ...
            self.myevent.clear()


# example of a class that uses two rotary encoders
class Application2():
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
        self.myevent = asyncio.Event()
        asyncio.create_task(self.action())
        r1.add_listener(self.callback)
        r2.add_listener(self.callback)

    def callback(self):
        self.myevent.set()

    async def action(self):
        while True:
            await self.myevent.wait()
            print('App 2:  rotary 1 = {}, rotary 2 = {}'. format(
                self.r1.value(), self.r2.value()))
            # do something with the encoder results ...
            self.myevent.clear()


async def main():
    rotary_encoder_1 = RotaryIRQ(pin_num_clk=13,
                                 pin_num_dt=14,
                                 min_val=0,
                                 max_val=5,
                                 reverse=False,
                                 range_mode=RotaryIRQ.RANGE_WRAP)

    rotary_encoder_2 = RotaryIRQ(pin_num_clk=18,
                                 pin_num_dt=19,
                                 min_val=0,
                                 max_val=20,
                                 reverse=False,
                                 range_mode=RotaryIRQ.RANGE_WRAP)

    # create tasks that use the rotary encoders
    app1 = Application1(rotary_encoder_1)
    app2 = Application2(rotary_encoder_1, rotary_encoder_2)

    # keep the event loop active
    while True:
        await asyncio.sleep_ms(10)

try:
    asyncio.run(main())
except (KeyboardInterrupt, Exception) as e:
    print('Exception {} {}\n'.format(type(e).__name__, e))
finally:
    ret = asyncio.new_event_loop()  # Clear retained uasyncio state
