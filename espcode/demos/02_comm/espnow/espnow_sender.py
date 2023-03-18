# ATTENTION: you need the firmware with ESP-NOW included!
# see documentation: https://micropython-glenn20.readthedocs.io/en/latest/library/espnow.html

import network
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()   # For ESP8266

e = espnow.ESPNow()
e.active(True)
peer = b'\xbb\xbb\xbb\xbb\xbb\xbb'   # MAC address of peer's wifi interface
e.add_peer(peer)

e.send("Starting...")       # Send to all peers
for i in range(100):
    e.send(peer, str(i)*20, True)
    e.send(b'end')
