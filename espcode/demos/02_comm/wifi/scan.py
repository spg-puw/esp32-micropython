import network
import binascii

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
results = wlan.scan()

security = {
    0: "open",
    1: "WEP",
    2: "WPA-PSK",
    3: "WPA2-PSK",
    4: "WPA/WPA2-PSK",
    5: "WPA2-Enterprise",
    6: "WPA3-PSK",
    7: "WPA2/WPA3-PSK",
    8: "WAPI-PSK",
    9: "OWE",
    10: "MAX",
}

print("found {} SSIDs:".format(len(results)))
for r in results:
    print("[{ishidden}] {ssid} ({bssid} @ Ch{chan} | {rssi}) with sec:{security}"
          .format(
              ssid = r[0].decode('ascii') or "<no name>",
              bssid = ':'.join([binascii.hexlify(r[1]).decode('ascii').upper()[i : i + 2] for i in range(0, 12, 2)]),
              chan = r[2],
              rssi = r[3],
              security = security[r[4]],
              ishidden = " " if not r[5] else "h"
          ))

