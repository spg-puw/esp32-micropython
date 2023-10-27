import machine
import time

led1 = machine.Pin(2, machine.Pin.OUT)
button1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

state = False
buttonHasBeenPressed = False

def irq_pushButton_bad(pin):
    global state
    time.sleep_ms(50) # 50ms warten (debounce) - ACHTUNG: sleep im IRQ ist schlecht!
    state = not state
    led1.value(state)

button1.irq(irq_pushButton_bad, machine.Pin.IRQ_FALLING) # irq bei fallender Flanke

def irq_pushButton_better(pin):
    # move processing and debouncing to main loop
    global buttonHasBeenPressed
    buttonHasBeenPressed = True

# button1.irq(irq_pushButton_better, machine.Pin.IRQ_FALLING) # irq bei fallender Flanke

while True:    
    if buttonHasBeenPressed == True:
        time.sleep_ms(50) # warten
        state = not state
        buttonHasBeenPressed = False
        
    led1.value(state)
