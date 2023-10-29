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
