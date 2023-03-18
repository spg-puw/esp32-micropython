# ESP32 mit MicroPython

## Allgemeines

Dieses Repository beinhaltet Democode für den ESP32 mit MicroPython.

## Struktur

* `espcode` beinhaltet den Code - die Dateien sollen/können in das Hauptverzeichnis am ESP32 geladen werden
  * in `espcode/lib` sind alle Bibliotheken (libraries) für alle Demo-Beispiele gespeichert
  * einige Bibliotheken müssen via WLAN und `upip` vom Internet heruntergeladen werden
  * in `espcode/static` und `espcode/templates` werden Dateien für den Webserverbetrieb (bspw. mit `picoweb`) ausgeliefert
* `firmware` beinhaltet die Firmware (sozusagen das Betriebssystem) für den ESP32; in der [Anleitung](Anleitung.pdf) wird gezeigt, wie die Firmware installiert werden kann.