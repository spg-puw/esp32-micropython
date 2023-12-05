'''
Verbindungen
Buzzer passiv (KY-006) ... ESP
-                          GND
S                          D25
'''

import machine
import time

# PWM signal starts with 1 Hz, you should hear a clicking
beep1 = machine.PWM(machine.Pin(25), freq=1, duty_u16=2**16//2)
time.sleep(3)

beep1.freq(100)
time.sleep_ms(1000)

beep1.freq(200)
time.sleep_ms(1000)

beep1.freq(400)
time.sleep_ms(1000)

beep1.freq(800)
time.sleep_ms(1000)

beep1.freq(1600)
time.sleep_ms(1000)

# stop the PWM signal - without deinit the signal will continue after program exits
beep1.deinit()
