import machine
import time

pushButtonBoot = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

for i in range(10):
    # wert = pushButtonBoot() # 1 wenn nichts gedrückt beim BOOT-Button
    wert = not pushButtonBoot() # 0 wenn nichts gedrückt beim BOOT-Button
    print("Der Button hat den Wert {wertVar}".format(wertVar=wert))
    time.sleep(1)
