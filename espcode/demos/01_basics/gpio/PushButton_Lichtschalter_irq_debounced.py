from machine import Pin
import time

led1 = Pin(2, Pin.OUT)
button1 = Pin(0, Pin.IN, Pin.PULL_UP)

state = False

def irq_pushButton(pin):
    global state
    time.sleep_ms(10) # 10ms warten (debounce)
    if pin.value() == 0:
        state = not state
        led1.value(state)

button1.irq(irq_pushButton, Pin.IRQ_FALLING)
