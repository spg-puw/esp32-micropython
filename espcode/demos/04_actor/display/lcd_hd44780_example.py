'''
Verkabelung mit I2C-LCD-Display
Display ... ESP32
GND         GND
VCC         Vin
SDA         D21
SCL         D22
'''

import machine
import time
from lcd_i2c import LCD

totalColumns = 16
totalRows = 2
i2cDisplayAdr = 0x27 # see i2c.scan(), PCF8574 on 0x50

i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21), freq=800000)
lcd = LCD(addr=i2cDisplayAdr, cols=totalColumns, rows=totalRows, i2c=i2c)

lcd.begin()
lcd.print("Hello World")
lcd.set_cursor(0,1)
lcd.print("cursor: ")
lcd.blink_on()
time.sleep(2)
lcd.cursor_on()
time.sleep(2)
lcd.blink_off()
time.sleep(2)
lcd.cursor_off()
time.sleep(2)
lcd.clear()
lcd.cursor_on()
lcd.print("XXXXXXXXXXXXXXXX hidden text")
lcd.home()
time.sleep(2)
lcd.print("overwrite")
time.sleep(2)
lcd.set_cursor(3,1)
lcd.print("scrolling ...")
time.sleep(2)

for _ in range(12):
    lcd.scroll_display_left()
    time.sleep(0.5)

time.sleep(5)

for _ in range(12):
    lcd.scroll_display_right()
    time.sleep(0.5)
    
time.sleep(2)
lcd.clear()
lcd.print("watch backlight")
time.sleep(2)
lcd.no_backlight()
time.sleep(2)
lcd.backlight()
time.sleep(2)

lcd.clear()
lcd.cursor_off()
# create your own char: https://maxpromer.github.io/LCD-Character-Creator/ --> outout as HEX
lcd.create_char(location=0, charmap=[0x00, 0x0A, 0x1F, 0x1F, 0x0E, 0x04, 0x00, 0x00])
lcd.set_cursor(7,0)
lcd.print(chr(0))
lcd.set_cursor(0,1)
lcd.print("InnoLab@Spengerg")
