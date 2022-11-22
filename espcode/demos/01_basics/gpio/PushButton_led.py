import utime as time
from machine import Pin

led1 = Pin(2, Pin.OUT)
button1 = Pin(0, Pin.IN)

# Light LED when (and while) a BUTTON is pressed

while True:
    led1.value(not button1.value())
    time.sleep_ms(10) # do not burn CPU