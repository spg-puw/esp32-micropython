import picoweb
import machine
import customnetwork
customnetwork.start()

led = machine.Pin(2, machine.Pin.OUT)
app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("""<button onclick="fetch('light')">Licht an</button><br>""")
    yield from resp.awrite("""<button onclick="fetch('nolight')">Licht aus</button><br>""")
    
@app.route("/light")
def lightFn(req, resp):
    yield from picoweb.start_response(resp)
    led.value(1)
    yield from resp.awrite("light")
    
@app.route("/nolight")
def noLightFn(req, resp):
    yield from picoweb.start_response(resp)
    led.value(0)
    yield from resp.awrite("nolight")

app.run(debug=True, host = customnetwork.getIP(), port = 80)
