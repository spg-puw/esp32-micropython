import picoweb
import ure as re
import customnetwork
customnetwork.setupSTA()

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    headers = {"X-IOTSpezial1": "super", "X-IOTAppBlob": "blub"}
    yield from picoweb.start_response(resp, headers=headers) #positional param would be more efficient
    yield from resp.awrite(b"""\
<!DOCTYPE html>
<html>
<head>
<link href="test.css" rel="stylesheet">
</head>
<body>
<p>style.css make yellow background and should be cached, might be encoded</p>
<p class="green">check out your webdev tool!</p>
</body>
</html>""")

@app.route(re.compile('^\/(.+\.css)$'))
def styles(req, resp):
    file_path = req.url_match.group(1)
    headers = b"Cache-Control: max-age=86400\r\n"

    #send gzipped content if supported by client
    #if b"gzip" in req.headers.get(b"Accept-Encoding", b""):
        #file_path += ".gz"
        #headers += b"Content-Encoding: gzip\r\n"

    print("sending " + file_path)
    yield from app.sendfile(resp, "static/" + file_path, "text/css", headers)

import ulogging as logging
logging.basicConfig(level=logging.INFO)

app.run(debug=True, host = customnetwork.getIP(), port = 80)