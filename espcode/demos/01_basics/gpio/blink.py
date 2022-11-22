from machine import Pin,Timer
import time

led = Pin(2, Pin.OUT)

while True:
    print("Schalte die interne LED ein")
    led.on()
    time.sleep(1)
    
    print("Schalte die interne LED aus")
    led.off()
    time.sleep(1)