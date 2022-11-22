from machine import Pin
import time

led1 = Pin(2, Pin.OUT) # interne LED
button1 = Pin(0, Pin.IN, Pin.PULL_UP) # Button BOOT
state = 0

while True:
    if button1.value() == 0:
        time.sleep_ms(10) # hier 10ms warten (debouncing)
        if button1.value() == 0:
            state = not state
            led1.value(state)
            while not button1.value():
                # nochmalige Ausführung verhindern
                pass
