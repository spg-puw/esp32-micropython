import machine
import time

watchdog = machine.WDT(timeout=2000)
for i in range(10):
    print("#{0}: wait for it ...".format(i))
    time.sleep(1)
    watchdog.feed()

print("2s left ...")
time.sleep(1.9)
print("now ...")
