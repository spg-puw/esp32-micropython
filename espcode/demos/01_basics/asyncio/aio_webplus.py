'''
Demo of how to use asyncio and picoweb together
picoweb uses asyncio

please also see picoweb examples in demos/02_comm/webserver
'''

import picoweb
import uasyncio as asyncio
from customnetwork import customnetwork
customnetwork.start()

async def loop_task():
    i = 0
    while True:
        i += 1
        print("Iterration {i}".format(i=i))
        # you can something else here
        await asyncio.sleep(1)

def index(req, resp):
    # your own headers
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    yield from resp.awrite("Go to <a href='test'>test</a>.<br/>")

def test_tmpl(req, resp):
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "test.tpl", (req, ))

ROUTES = [
    ("/", index),
    ("/test", test_tmpl),
]

loop = asyncio.get_event_loop()
loop.create_task(loop_task())
# you can start some other tasks here

app = picoweb.WebApp(__name__, ROUTES)
app.run(debug=True, host = customnetwork.getIP(), port = 80)