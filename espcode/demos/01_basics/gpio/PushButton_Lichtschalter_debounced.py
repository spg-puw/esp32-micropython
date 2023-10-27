import machine
import time

led1 = machine.Pin(2, machine.Pin.OUT) # interne LED
button1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP) # Button BOOT
state = 0

while True:
    if button1.value() == 0:
        time.sleep_ms(10) # hier 10ms warten (debouncing)
        if button1.value() == 0: # nochmals pruefen
            state = not state # Zustand umschalten
            led1.value(state)
            while not button1.value():
                # nochmalige Ausführung verhindern
                pass
