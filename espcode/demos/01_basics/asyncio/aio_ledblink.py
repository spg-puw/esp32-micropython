'''
Lässt 3 LEDs gleichzeitig blinken

Anschlüsse:

LED1 ... interne LED
LED2 ... Pin D12
LED3 ... Pin D14
'''

import machine
import uasyncio as asyncio

led1 = machine.Pin(2, machine.Pin.OUT)
led2 = machine.Pin(12, machine.Pin.OUT)
led3 = machine.Pin(14, machine.Pin.OUT)

async def toggleLed(led, duration = 1):
    while True:
        await asyncio.sleep(duration)
        led.toggle() # LED umschalten

async def starteAsync():
    await asyncio.gather(
        toggleLed(led1, 1), # freq = 0.5 Hz
        toggleLed(led2, 0.4), # freq = 1.25 Hz
        toggleLed(led3, 0.5), # freq = 1.0 Hz
    )

asyncio.run(starteAsync())
