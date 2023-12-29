'''
see: https://github.com/miguelgrinberg/microdot/blob/main/examples/websocket/echo.py
'''

from microdot import Microdot, send_file
from microdot.websocket import with_websocket

app = Microdot()

@app.route('/')
async def index(request):
    return send_file('static/ws.html')

@app.route('/echo')
@with_websocket
async def echo(request, ws):
    while True:
        data = await ws.receive()
        await ws.send(data)

app.run(debug=True)
