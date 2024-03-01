# Displays

## LCD1602

* ein LCD-Display mit 16x2 Zeichen Anzeigefläche ([Datenblatt](https://www.vishay.com/docs/37484/lcd016n002bcfhet.pdf))
* bekannt unter folgenden Bezeichnungen: LCD1602, LCD2004
* Displaytriber ist der HD44780 ([Datenblatt](https://www.mouser.com/datasheet/2/737/HD44780-2489576.pdf))
* die Displays haben viele Anschlusspins und man kann den HD44780 direkt ansteuern
* mit dem PCF8574-I2C Wandler kann das Display via I2C angesteuert werden
* die Bibliothek findet sich [hier](https://github.com/brainelectronics/micropython-i2c-lcd/) bzw. [hier](https://pypi.org/project/micropython-i2c-lcd/) inkl. [Dokumentation](https://micropython-i2c-lcd.readthedocs.io/en/latest/index.html)
* eigene Zeichen können bspw. mit diesem [Onlinetool](https://maxpromer.github.io/LCD-Character-Creator/) erstellt werden (bei der Ausgabe `data type: HEX` auswählen)

Die Bibliothek kann automatisch wie folgt installiert werden:

```python
import mip
mip.install("github:brainelectronics/micropython-i2c-lcd")
```

## Waveshare ePaper Display 2.13in (250x122)

siehe [hier](https://www.waveshare.com/wiki/Pico-ePaper-2.13) und [hier](https://github.com/waveshareteam/Pico_ePaper_Code)

* monochromes Display
* 250x122 Pixel Auflösung
* SPI

## Waveshare Pico LCD 2

siehe [hier](https://www.waveshare.com/wiki/Pico-LCD-2) und [hier](https://files.waveshare.com/upload/5/5f/Pico-LCD-2_SchDoc.pdf)

* Display 2"
* 320px x 240px
* 65k colors
* SPI
* [ST7789VW](https://files.waveshare.com/upload/a/ad/ST7789VW.pdf) Treiber
* 4x user button

**Achtung**: Der Framebuffer wurde reduziert, da zu viel Memory gebraucht wird!