# MicroPython asyncio (uasyncio)

## Einführung

Die offizielle Dokumentation von `uasyncio` in MicroPython findet sich [hier](https://docs.micropython.org/en/latest/library/asyncio.html).

> CPython supports asynchronous programming via the asyncio library. MicroPython provides uasyncio which is a subset of this, optimised for small code size and high performance on bare metal targets. This repository provides documentation, tutorial material and code to aid in its effective use.

Weitere Informationen siehe auch [hier](https://github.com/peterhinch/micropython-async/tree/master) und [hier](https://github.com/peterhinch/micropython-async/blob/master/v3/README.md).
Ein detailiertes Tutorial mit vielen Beispielen und Erklärungen findet man [hier](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md).

## Installation

Ab MicroPython v1.13 ist uasyncio (V3) bereits enthalten und kann mit `import uasyncio` eingebunden werden. Leider sind Semaphoren und Queues noch nicht nativ implementiert, eine inoffizielle Implementierung hat [Peter Hinch auf GitHub](https://github.com/peterhinch/micropython-async/tree/master/v3/primitives). Die Installation erfolgt wie folgt ([original hier](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md#01-installing-asyncio-primitives)):

```python
import mip
mip.install("github:peterhinch/micropython-async/v3/primitives")
mip.install("github:peterhinch/micropython-async/v3/threadsafe")
```

Die Dateien werden beim automatischen Setup schon mitinstalliert, zu Dokumentationszwecken trotzdem extra:
* https://github.com/peterhinch/micropython-async/blob/master/v3/primitives/package.json
* https://github.com/peterhinch/micropython-async/blob/master/v3/threadsafe/package.json
