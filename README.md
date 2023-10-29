# ESP32 mit MicroPython

## Allgemeines

Dieses Repository beinhaltet Democode für den ESP32 mit MicroPython. Anfängern wird empfohlen mit der IDE [Thonny](https://thonny.org/) zu arbeiten.

## Struktur

* `espcode` beinhaltet den Code - die Dateien sollen/können in das Hauptverzeichnis am ESP32 geladen werden
  * in `espcode/demos` sind einige Beispiele
  * in `espcode/lib` sind alle Bibliotheken (libraries) für alle Demo-Beispiele gespeichert
  * einige Bibliotheken müssen via WLAN und `mip` vom Internet heruntergeladen werden
  * in `espcode/static` und `espcode/templates` werden Dateien für den Webserverbetrieb (bspw. mit `picoweb`) ausgeliefert
* `firmware` beinhaltet die Firmware (sozusagen das Betriebssystem) für den ESP32; in der [Anleitung](Anleitung.pdf) wird gezeigt, wie die Firmware installiert werden kann
  * die aktuellste Firmware kann mit der IDE Thonny automatisch heruntergeladen und installiert werden (siehe [Anleitung](Anleitung.pdf))
  * damit der ESP mit dem Computer via USB kommunizieren kann, müssen entsprechende Treiber installiert werden. Mehr Informationen [hier](firmware)

## Setup des ESP

Viele Beispiele können natürlich ohne Internetzugang des ESP benutzt werden - die Abhängigkeiten (v.a. Bibliotheken in `/lib/`) müssen dann selber installiert/kopiert werden.

**Automatisches Setup**: Es gibt ein Setup-Skript (siehe [hier](setupESP.py)), welches

1. den ESP32 mit dem WLAN verbindet (Zugangsdaten werden benötigt: SSID, Passwort)<br>Die Verbindung wird nach einem Neustart des ESP automatisch wieder hergestellt (siehe `boot.py`)
2. die notwendigen Abhängigkeiten automatisch herunterlädt und auf dem ESP32 speichert

Kopieren Sie den Code aus dem Setup-Skript `setupESP.py` und führen Sie diesen auf dem ESP32 aus. Das Setupprogramm fragt über die Shell einige Informationen ab, verbindet sich mit dem WLAN und installiert die Abhängigkeiten.

## Verbesserungsvorschläge und Mitarbeit

Sie wollen Mitarbeiten und haben ...?

* neue nützliche Treiber
* interessante Beispiele
* Fehler gefunden
* sonstige Verbesserungsvorschläge oder Anregungen

Zögern Sie nicht und kontaktieren Sie den Repo-Besitzer unter innolab@spengergasse.at oder erstellen Sie Issues/PR (pull request).
