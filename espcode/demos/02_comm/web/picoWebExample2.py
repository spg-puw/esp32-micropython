#
# This is a picoweb example showing a centralized web page route
# specification (classical Django style).
#
import ure as re
import picoweb
import customnetwork
customnetwork.setupSTA()


def index(req, resp):
    # You can construct an HTTP response completely yourself, having
    # a full control of headers sent...
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    yield from resp.awrite("See a <a href='templ'>template</a><br/>")
    yield from resp.awrite("Or see a <a href='file'>file</a><br>")
    yield from resp.awrite("Or try <a href='iam/Hans/Wurst/x/bla/bla/'>regex</a>")


def templ(req, resp):
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "test.tpl", (req,))


def rexcheck(req, resp):
    yield from picoweb.start_response(resp)
    data = req.url_match.group(1) #Hans/Wurst
    yield from resp.awrite("Hello " + data.replace("/", " ")) #Hans Wurst


ROUTES = [
    ("/", index),
    ("/templ", templ),
    ("/file", lambda req, resp: (yield from app.sendfile(resp, "static/hello.txt"))),
    (re.compile("^/iam/(.+)/x/(.+)"), rexcheck),
]

import ulogging as logging
logging.basicConfig(level=logging.INFO) #logging.DEBUG
app = picoweb.WebApp(__name__, ROUTES)
# debug values:
# -1 disable all logging
# 0 (False) normal logging: requests and errors
# 1 (True) debug logging
# 2 extra debug logging
app.run(debug=True, host = customnetwork.getIP(), port = 80)