from machine import Pin,Timer

led1 = Pin(2, Pin.OUT)

counter = 0

def callback_function(t):
    global counter
    counter = counter + 1
    print(counter)
    led1.value(counter % 2)

timer1 = Timer(-1)
timer1.init(period=1000, mode=Timer.PERIODIC, callback=callback_function)
