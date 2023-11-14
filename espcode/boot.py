# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

try:
    from customnetwork import customnetwork
    customnetwork.start()
except Exception as e:
    print("error in boot.py: {0}".format(e))
finally:
    del customnetwork
    gc.collect()