import picoweb
from customnetwork import customnetwork
customnetwork.start()
 
app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Demo ")
    yield from resp.awrite("""Hallo <a href="link">Welt</a>""")
 
app.run(debug=True, host = customnetwork.getIP(), port = 80)