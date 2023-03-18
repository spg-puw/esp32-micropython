# MicoPython Firmware für den ESP32

## Vanilla Firmware

Die Firmware für den ESP32 kann unter [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/) heruntergeladen werden.

Die Dokumentation ist unter folgenden Links zu finden:

* https://docs.micropython.org/en/latest/
* https://docs.micropython.org/en/latest/esp32/quickref.html

## Firmware mit ESP-NOW

ESP-NOW ist ein Funkprotokoll von Espressif, welches auf 2.4 GHz operiert. Die |[Dokumentation](https://www.espressif.com/en/products/software/esp-now/overview) des Herstellers ist hier zu finden.

In der Vanilla Firmware ist das Protokoll (noch) nicht implementiert, es wird daher ein vorkompiliertes Firmware-Image vom GitHub User `glenn20` empfohlen.

* Nähere Informationen finden sich im entsprechenden [Repository](https://github.com/glenn20/micropython/tree/espnow-g20)
* Die Images finden sich [hier](https://github.com/glenn20/micropython-espnow-images)
* Die Dokumentation ist [hier](https://micropython-glenn20.readthedocs.io/en/latest/library/espnow.html) zu finden
* Aktuelle Version: [hier](https://github.com/glenn20/micropython-espnow-images/blob/main/latest)
* Ein Downloadlink aus dem Repository von Benutzer `glenn20`: [hier](https://github.com/glenn20/micropython-espnow-images/blob/main/20220709_espnow-g20-v1.19.1-espnow-6-g44f65965b/firmware-esp32-GENERIC.bin)