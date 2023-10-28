import picoweb
import customnetwork
customnetwork.start()

app = picoweb.WebApp(__name__)

@app.route("/form_url")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET?
        req.parse_qs() #parse query string

    #form data in req.form
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello %s!" % req.form["name"])

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("POST form:<br>")
    yield from resp.awrite("<form action='form_url' method='POST'>"
        "What is your name? <input name='name' /> "
        "<input type='submit'></form>")

    yield from resp.awrite("GET form:<br>")
    yield from resp.awrite("<form action='form_url'>"
        "What is your name? <input name='name' /> "
        "<input type='submit'></form>")

import ulogging as logging
logging.basicConfig(level=logging.INFO)

app.run(debug=True, host = customnetwork.getIP(), port = 80)