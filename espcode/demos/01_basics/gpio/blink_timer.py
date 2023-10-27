import machine

led1 = machine.Pin(2, machine.Pin.OUT)

counter = 0

def callback_function(t):
    global counter
    counter = counter + 1
    print(counter)
    led1.value(counter % 2)

timer1 = machine.Timer(-1)
timer1.init(period=1000, mode=machine.Timer.PERIODIC, callback=callback_function)

print("program execution ends here, but the timer continues")
