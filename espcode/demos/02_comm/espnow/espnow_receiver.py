# ATTENTION: you need the firmware with ESP-NOW included!
# see documentation: https://micropython-glenn20.readthedocs.io/en/latest/library/espnow.html

import network
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

e = espnow.ESPNow()
e.active(True)
peer = b'\xaa\xaa\xaa\xaa\xaa\xaa'   # MAC address of peer's wifi interface
e.add_peer(peer)

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        print(host, msg)
        if msg == b'end':
            break
