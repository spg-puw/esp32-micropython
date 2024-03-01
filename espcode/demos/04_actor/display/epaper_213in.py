'''
Waveshare ePaper Display (see https://www.waveshare.com/wiki/Pico-ePaper-2.13)

Display 2.13" (250px x 122px)
Display ... RPi pico
VCC         VSYS    Power input
GND         GND     Ground
DIN         GP11    MOSI pin of SPI interface, data transmitted from Master to Slave.
CLK         GP10    SCK pin of SPI interface, clock input
CS          GP9     Chip select pin of SPI interface, Low Active
DC          GP8     Data/Command control pin (High: Data; Low: Command)
RST         GP12    Reset pin, low active
BUSY        GP13    Busy output pin
KEY0        GP2     User key 0
KEY1        GP3     User key 1
RUN         RUN     Reset 
'''

import math
from waveshare_epaper213 import EPD_2in13_V4_Landscape

epd = EPD_2in13_V4_Landscape()
epd.Clear()

epd.fill(0xff)
epd.text("HTL Spengergasse", 63, 90, 0x00)
epd.text("ausbildung mit zukunft", 40, 100, 0x00)
epd.hline(10, 112, 230, 0x00)
epd.text("InnoLab", 100, 115, 0x00)    
epd.display(epd.buffer)
epd.delay_ms(2000)

center = (125, 50)
d1 = 15
d2 = 15
for i in range(0, 5):
    alpha = i * (2 * math.pi)/5 - math.pi/2
    x, y = center
    epd.line(x + int(d1 * math.cos(alpha)), y + int(d1 * math.sin(alpha)), (x + int(d1 * math.cos(alpha))) + (int(d2*math.cos(alpha))), y + int(d1 * math.sin(alpha)) + (int(d2*math.sin(alpha))), 0x00)

epd.display(epd.buffer)
epd.delay_ms(2000)
