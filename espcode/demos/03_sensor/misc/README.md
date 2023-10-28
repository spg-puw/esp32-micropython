# Weitere Sensoren

Für einige Sensoren werden Bibliotheken benötigt.

## KY-001 - DS18B20 (Temperatursensor)

Der Sensor kommuniziert über OneWire. Die Bibliothek des Sensors ist bereits in MicroPython integriert. Siehe [hier](https://docs.micropython.org/en/latest/esp32/quickref.html#onewire-driver).

## KY-015 - DHT11 (Temperatur und Luftfeuchte)

Die Bibliothek des Sensors ist bereits in MicroPython integriert. Siehe [hier](https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver).

## KY-052 - BMP280 (Temperatur und Luftdruck)

Kopieren Sie `lib/bmp280.py` auf den ESP32.

## MPU6050 (Beschleunigungssensor)

Kopieren Sie `lib/mpu6050.py` auf den ESP32.
