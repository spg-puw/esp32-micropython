'''
Verbindung von KY-023 (Joystick)
Joystick ... ESP
GND          GND
+5V          3V3
VRx          D34
VRy          D35
SW           D32

GPIOs für ADC Block 1: 32, 33, 34, 35, 36 und 39
GPIOs für ADC Block 2: keine - WLAN wird benutzt, daher ist Block 2 nicht verfügbar
'''

import machine
import time
import picoweb

from customnetwork import customnetwork
customnetwork.start()

# 1) Beim ESP-Aufruf kommt die Webseite (HTML + JS Code)
# 2) Joystick anschließen und bei einem Webseitenaufruf
#       http://IP-AdresseVomESP32/getJoystick
#    kommt ein JSON im Format: {"x":X-PROZENT,"y":Y-PROZENT,"pressed":"True/False"}
#

app = picoweb.WebApp(__name__)

joyX = machine.Pin(34, machine.Pin.IN)
joyY = machine.Pin(35, machine.Pin.IN)
joyButton = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

joyXadc = machine.ADC(joyX)
joyXadc.atten(machine.ADC.ATTN_11DB)
joyYadc = machine.ADC(joyY)
joyYadc.atten(machine.ADC.ATTN_11DB)

@app.route("/getJoystick")
def index(req, resp):
    headers = {"Access-Control-Allow-Origin": "*", "X-IOT": "1"}
    yield from picoweb.start_response(resp, headers=headers)
    
    valX = joyXadc.read()  # unsigned integer mit range 0-4095
    valY = joyYadc.read()  # unsigned integer mit range 0-4095 
    buttonPressed = not joyButton.value()   
    yield from resp.awrite("{" + """"x":{wertX},"y":{wertY},"pressed":"{btn}""".format(wertX=valX, wertY=valY, btn=buttonPressed) + "\"}")

@app.route("/") # / ist die Hauptseite
def index(req, resp):
    #yield from picoweb.start_response(resp)
    
    # hier laden wir die Webseite aus dem Speicher (unter static/ )
    yield from app.sendfile(resp, "static/joystick1.html", "text/html")

app.run(debug=True, host = customnetwork.getIP(), port = 80)
