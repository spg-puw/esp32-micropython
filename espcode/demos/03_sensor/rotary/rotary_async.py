'''
Verkableung KY-040 (Rotary Encoder)
KY-040 ... ESP32
CLK        D13
DT         D14
SW         (nicht verbunden, SW ... switch ... ist der Button)
+          3V3
GND        GND
'''

import machine
import sys
from rotary_irq_esp import RotaryIRQ
import uasyncio as asyncio

led1 = machine.Pin(2, machine.Pin.OUT)

# Use heartbeat to keep event loop not empty
async def heartbeat():
    while True:
        await asyncio.sleep_ms(5000)
        print("Schleife ...")
        
async def blink():
    while True:
        await asyncio.sleep_ms(1000)
        led1.value(1)
        await asyncio.sleep_ms(1000)
        led1.value(0)

event = asyncio.Event()

def callback():
    event.set()

async def main():
    r = RotaryIRQ(pin_num_clk=13,
                  pin_num_dt=14)
    r.add_listener(callback)
    
    asyncio.create_task(heartbeat())
    asyncio.create_task(blink())
    while True:
        await event.wait()
        print('result =', r.value())
        event.clear()

try:
    asyncio.run(main())
except (KeyboardInterrupt, Exception) as e:
    print('Exception {} {}\n'.format(type(e).__name__, e))
finally:
    ret = asyncio.new_event_loop()  # Clear retained uasyncio state
