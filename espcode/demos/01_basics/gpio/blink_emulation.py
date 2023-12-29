'''
this example shows how to emulate a simple LED when you have no real hardware
the information will be printed to the console
'''

import time

class LEDClass:
    def __init__(self, pin):
        self.showDebug = False
        self.pin = pin
        self.val = False
        self.id = "LED (Pin {}):".format(pin)

    def __str__(self):
        return "{} {}".format(self.id, self.val)

    def value(self, v = None):
        if v is not None:
            if self.showDebug:
                print(self.id, "setting value to", v)
            self.val = v
        return self.val

    def on(self):
        self.value(True)

    def off(self):
        self.value(False)

    def toggle(self):
        self.value(not self.value())


led1 = LEDClass(2)
led2 = LEDClass(25)

led1.on()
led1.showDebug = True
led1.off()
led1.on()
led2.value(2)
print(led1)
print(led2)

for _ in range(20):
    led1.toggle()
    time.sleep(0.5)
