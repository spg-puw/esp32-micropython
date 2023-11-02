import machine
import time
try:
    import esp32
except:
    print("only esp32 supported!")

def main():
    if machine.wake_reason() == machine.DEEPSLEEP:
        print("i woke up from deepsleep")
    else:
        print("i woke up ... reason: {0}".format(machine.wake_reason()))

    # Some ESP32 pins (0, 2, 4, 12-15, 25-27, 32-39) are connected to the RTC
    # during deep-sleep and can be used to wake the device with the wake_on_
    # functions in the esp32 module. The output-capable RTC pins (all except 34-39)
    # will also retain their pull-up or pull-down resistor configuration when
    # entering deep-sleep.
    # Non-RTC GPIO pins will be disconnected by default on entering deep-sleep.
    # Configuration of non-RTC pins - including output level - can be retained by
    # enabling pad hold on the pin and enabling GPIO pad hold during deep-sleep.
    # see: https://docs.micropython.org/en/latest/esp32/quickref.html#deep-sleep-mode

    # setup some useless pins
    ledIntern = machine.Pin(2, machine.Pin.OUT, value=1)
    pin12 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
    pin19 = machine.Pin(19, machine.Pin.OUT, value=1, hold=True) # hold output level
    pin21 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP, hold=True) # hold pull-up
    esp32.gpio_deep_sleep_hold(True) # enable pad hold in deep-sleep for non-RTC GPIO
    
    print("=====")
    print("i will go to lightsleep for 10s")
    print("machine.sleep will not empty the output buffer")
    # time.sleep(0.1)

    machine.sleep(5000) # machine.sleep and machine.lightsleep are the same
    machine.lightsleep(5000) # program state is retained and execution will continue

    pin12.init(pull=None) # stop pullup to save energy
    
    for _ in range(10):
        print("very, very, very long string")
        
    print("i will go to deepsleep for 10s")
    
    machine.deepsleep(10000) # put the device to sleep for 10 seconds
    
    # ledIntern will be turned off; also check pins 12, 19 and 21!
    # ATTENTION: everything after deepsleep never gets executed
    print("you will never see this line")

if __name__=="__main__":
    main()
