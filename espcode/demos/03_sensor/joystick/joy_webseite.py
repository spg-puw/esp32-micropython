import picoweb
import customnetwork
import machine
import time
customnetwork.setupSTA()

# 1) Beim ESP-Aufruf kommt die Webseite (HTML + JS Code)
# 2) Joystick anschließen und bei einem Webseitenaufruf
#       http://IP-AdresseVomESP32/joy
#    kommt ein JSON im Format: {"x":X-PROZENT,"y":Y-PROZENT}
#

app = picoweb.WebApp(__name__)

i = 1

joyX = machine.Pin(34, machine.Pin.IN)
joyY = machine.Pin(35, machine.Pin.IN)

joyXadc = machine.ADC(joyX)
joyXadc.atten(machine.ADC.ATTN_11DB) #Lesebereich 0 bis 3,3 V
joyYadc = machine.ADC(joyY)
joyYadc.atten(machine.ADC.ATTN_11DB) #Lesebereich 0 bis 3,3 V

@app.route("/joystick")
def index(req, resp):
    headers = {"Access-Control-Allow-Origin": "*", "X-IOT": "1"}
    yield from picoweb.start_response(resp, headers=headers)
    
    valX = joyXadc.read()  #unsigned integer mit range 0-4095
    valY = joyYadc.read()  #unsigned integer mit range 0-4095    
    yield from resp.awrite("{"     +     """"x":{wertX},"y":{wertY}""".format(wertX=valX, wertY=valY)    +    "}")

@app.route("/") #/ ist die Hauptseite
def index(req, resp):
    yield from picoweb.start_response(resp)
    
    #hier laden wir die Webseite aus dem Speicher (unter static/ )
    yield from app.sendfile(resp, "static/joystick1.html", "text/html")

app.run(debug=True, host = customnetwork.getIP(), port = 80)
