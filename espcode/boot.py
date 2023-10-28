# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

try:
    from customnetwork import customnetwork
    customnetwork.start()
    del customnetwork
    gc.collect()
except:
    print("error in boot.py")
