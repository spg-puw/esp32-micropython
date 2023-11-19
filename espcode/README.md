# Spengergasse InnoLab ESP32 Samples

Diese Repository enthält Democode für den ESP32 zur Benutzung im InnoLab.

## Benötigte Software

* [Thonny (IDE)](https://thonny.org/)
* [USB-Treiber](./../firmware/driver/)

## Nützliche Links

* [ESP32 Datenblatt](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
* [ESP32 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)
* [MicroPython Dokumentation](https://docs.micropython.org/en/latest/esp32/quickref.html)
* [Sensorkit X40](https://sensorkit.joy-it.net/de/)

## Verwendete Sensoren und Aktoren aus dem Sensorkit X40

* KY-001 - DS18B20 (Temperatursensor)
* KY-004 - Button
* KY-006 - Passiver Piezo-Buzzer
* KY-015 - DHT11 (Temperatur und Luftfeuchte)
* KY-018 - LDR (Fotowiderstand)
* KY-023 - Joystick
* KY-040 - Rotary Encoder
* KY-052 - BMP280 (Temperatur und Luftdruck)

## Zusätzliche Sensoren, Aktoren und Materialien

Sensoren:

* MPU6050 - Beschleunigungssensor
* MFRC522 - RFID-Reader

Aktoren:

* LED-Streifen mit 15 Stk. WS2812B LEDs
* Div. LEDs inkl. Vorwiderstand
* Stepper Motor 28BYJ-48 mit Treiberboard und Treiberchip ULN2003
* Servomotor SG90
* LCD Display 16x02 (LCD1602) mit I2C-Board

Kabel:

* 10 Verbindungskabel (f-f)

## Inspirationsgrundlage für Beispiele und Aufgaben

Ein besonderer Dank gilt meinem Kollegen *PUA* für die zahlreichen Ideen.

### Beispiele und Aufgaben (IOT)

* Grundlagen: Mikrocontroller kennenlernen, Steckbrett, Verkabelung etc.; Erweiterung mit Messung Widerstandsnetzwerke und Simulation
* Morsen: GPIOs kontrollieren (LED, Button); MicroPython kennenlernen
* Verkehrsampel (LEDs über GPIOs oder Neopixel LED-Leuchtstreifen mit WS2812B); Erweiterung mit Fußgängerampel; Erweiterung mit Theorie zu state machines
* Kommunikationsprotokolle: ESP-ESP Kommunikation, ESP+Sensor; UART, SPI, I2C; Erweiterung mit Oszi; Erweiterung mit [PulseView](https://sigrok.org/wiki/PulseView)
* Sirene: Passivbuzzer und Drehgeber (rotary encoder) oder Poti (via ADC) zur Frequenzauswahl
* Einparkhilfe: Ultraschallabstandssensor und Aktivbuzzer; Distanz wird akustisch ausgegeben
* Tagfahrlicht: RGB-LED mit PWM (oder WS2812B), LDR (KY-018) mit ADC, eine RGB-LED soll abhängig von der Umgebungslichtstärke die Helligkeit erhöhen; Erweiterung mit Button zum Aktivieren/Deaktivieren der Funktion
* Schranke: RFID-Kartenleser, Taster und Servomotor; Schranke wird mittels Taster geöffnet und geschlossen; RFID-Tag (z.B. educard) öffnet automatisch und schließt zeitverzögert, Taster entprellen, IDs der Tags in einer Textdatei speichern; Erweiterung durch Webanwendung: anlernen neuer Tags über Weboberfläche
* Scheibenwischer: DHT11, Steppermotor, Schrittmotor soll abhängig von der Luftfeuchtigkeit die Geschwindigkeit einer Scheibenwischbewegung variieren
* Autoradio: Joystick (mit ADC), LCD-Display (16x2); Lautstärke, Frequenz und Modulationsart eines Autoradios soll mittels Joystick eingestellt und Display angezeigt werden können

### Erweiterungen

Die Beispiele können nach Bedarf natürlich immer erweitert werden:

* Erweiterung mit UART: z.B. Ausgabe von Werten jede Sekunde
* Erweiterung mit Bluetooth: z.B. Sensorwerte/Zustand auslesen, Steuerung (on/off), Setzen von Parametern
* Erweiterung mit Weboberfläche: z.B. Daten via API zugänglich machen oder Webseite mit Template bauen
* Erweiterung mit MQTT: z.B. Werte publishen, auf Nachrichten reagieren
* Erweiterung mit Gehäuse: Gehäuse für Display, Sensoren o.ä. inkl. 3D-Druck/Lasercutting
