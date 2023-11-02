'''
Leuchtstreifen mit 15 Stk. WS2812B LEDs

Dokumentation: https://docs.micropython.org/en/latest/library/neopixel.html

Verkabelung:
Leuchstreifen ... ESP32
+5V .............. Vin
D0 ............... D13
GND .............. GND

Anmerkung: probiere auch WLED aus (https://install.wled.me/)
'''

import machine
import time
import neopixel

anzahlLeds = 15
leuchtstreifenPin = machine.Pin(13, machine.Pin.OUT)
np = neopixel.NeoPixel(leuchtstreifenPin, anzahlLeds)

def demo(np):
    n = np.n

    # kitt
    delay = 50
    for _ in range(4):
        for i in range(0, n, 1):
            for j in range(n):
                np[j] = (0, 0, 0)
            if i > 0:
                np[i - 1] = (20, 0, 0)
            if i > 1:
                np[i - 2] = (1, 0, 0)
            if i < (n - 1):
                np[i + 1] = (20, 0, 0)
            if i < (n - 2):
                np[i + 2] = (1, 0, 0)
            np[i % n] = (255, 0, 0)
            np.write()
            time.sleep_ms(delay)
        time.sleep_ms(200)
        for i in range(n, 0, -1):
            i -= 1
            for j in range(n):
                np[j] = (0, 0, 0)
            if i > 0:
                np[i - 1] = (20, 0, 0)
            if i > 1:
                np[i - 2] = (1, 0, 0)
            if i < (n - 1):
                np[i + 1] = (20, 0, 0)
            if i < (n - 2):
                np[i + 2] = (1, 0, 0)
            np[i % n] = (255, 0, 0)
            np.write()
            time.sleep_ms(delay)
        time.sleep_ms(200)

    # cycle
    for i in range(5 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    for i in range(5 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(5 * n):
        for j in range(n):
            np[j] = (0, 128, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 20 * 256):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

if __name__=="__main__":
    demo(np)
