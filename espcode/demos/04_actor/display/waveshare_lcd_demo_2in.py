'''
Waveshare Pico LCD 2 (see https://www.waveshare.com/wiki/Pico-LCD-2)
Display 2" (320px x 240px, 65k colors, SPI, ST7789VW)

LCD ... RPi pico
VCC     VSYS    Power Input
GND     GND     Ground
DIN     GP11    MOSI pin of SPI, data transmitted from Master t Slave
CLK     GP10    SCK pin of SPI, clock pin
CS      GP9     Chip selection of SPI, low active
DC      GP8     Data/Command control pin (High for data; Low for command)
RST     GP12    Reset pin, low active
BL      GP13    Backlight control
KEY0    GP15    User button KEY0
KEY1    GP17    User button KEY1
KEY2    GP2     User button KEY2
KEY3    GP3     User button KEY3 
'''

import math
import machine
import time
from waveshare_lcd2in import LCD_2inch

key0 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP) 
key1 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
key2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
key3 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

brightness = machine.PWM(machine.Pin(13))
brightness.freq(1000)
brightness.duty_u16(30000) # max 65535

LCD = LCD_2inch()
LCD.fill(LCD.WHITE)

time.sleep(0.1)
LCD.fill_rect(0, 0, 320, 15, LCD.RED)
LCD.fill_rect(0, 0, 15, 240, LCD.RED)
LCD.fill_rect(320-15, 0, 320, 240, LCD.RED)
LCD.fill_rect(0, 240-40, 320, 240, LCD.RED)
LCD.text("HTL Spengergasse", 100, 90, 0x00)
LCD.text("ausbildung mit zukunft", 75, 100, 0x00)
LCD.hline(20, 112, 320-20-20, 0x00)
LCD.text("InnoLab", 135, 115, 0x00)

center = (int(320/2), 50)
d1 = 15
d2 = 15
for i in range(0, 5):
    alpha = i * (2 * math.pi)/5 - math.pi/2
    x, y = center
    LCD.line(x + int(d1 * math.cos(alpha)), y + int(d1 * math.sin(alpha)), (x + int(d1 * math.cos(alpha))) + (int(d2*math.cos(alpha))), y + int(d1 * math.sin(alpha)) + (int(d2*math.sin(alpha))), LCD.RED)

time.sleep(0.1)
LCD.show()
LCD.fill(0xFFFF)
time.sleep(5)

while(True):      
    if(key0.value() == 0):
        LCD.fill_rect(12, 12, 20, 20, LCD.RED)
    else :
        LCD.fill_rect(12, 12, 20, 20, LCD.WHITE)
        LCD.rect(12, 12, 20, 20, LCD.RED)
        
    if(key1.value() == 0):
        LCD.fill_rect(288, 12, 20, 20, LCD.RED)
    else :
        LCD.fill_rect(288, 12, 20, 20, LCD.WHITE)
        LCD.rect(288, 12, 20, 20, LCD.RED)
        
    if(key2.value() == 0):
        LCD.fill_rect(288, 208, 20, 20, LCD.RED)
    else :
        LCD.fill_rect(288, 208, 20, 20, LCD.WHITE)
        LCD.rect(288, 208, 20, 20, LCD.RED)
    
    if(key3.value() == 0):
        LCD.fill_rect(12, 208, 20, 20, LCD.RED)
    else :
        LCD.fill_rect(12, 208, 20, 20, LCD.WHITE)
        LCD.rect(12, 208, 20, 20, LCD.RED) 
                  
    LCD.show()

time.sleep(1)
LCD.fill(0xFFFF)
