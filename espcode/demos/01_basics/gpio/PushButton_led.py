import machine
import time

led1 = machine.Pin(2, machine.Pin.OUT)
button1 = machine.Pin(0, machine.Pin.IN)

# Light LED when (and while) a BUTTON is pressed

while True:
    led1.value(not button1.value())
    time.sleep_ms(10) # do not burn CPU