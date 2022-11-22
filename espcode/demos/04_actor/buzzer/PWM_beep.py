from machine import Pin, PWM
import time

beep1 = PWM(Pin(25), freq=0, duty=512)

beep1.freq(200)
time.sleep_ms(1000)

beep1.freq(400)
time.sleep_ms(1000)

beep1.freq(600)
time.sleep_ms(1000)

beep1.freq(800)
time.sleep_ms(1000)

beep1.freq(1000)
time.sleep_ms(1000)

beep1.deinit()
