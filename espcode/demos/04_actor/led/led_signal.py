import machine

# active low .... LOW Pegel schaltet die LED ein ---> LOW  = leuchten
# active high ... HIGH Pegel schaltet die LED ein --> HIGH = leuchten

led1pin = machine.Pin(2, machine.Pin.OUT) # active-high LED
led2pin = machine.Pin(4, machine.Pin.OUT) # active low LED

# make them light up
led1pin.value(1)
led2pin.value(0)

# signal class abstracts active-high/active-low away
led1 = machine.Signal(led1pin, invert=False)
led2 = machine.Signal(led2pin, invert=True)

# make them light up
led1.value(1)
led2.value(1)
led1.on()
led2.on()

