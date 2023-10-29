import socket

def web_page():
  html = """<html><head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      padding: 20px;
      margin: auto;
      width: 50%;
      text-align: center;
    }
  </style>
</head><body>
  <h1>MicroPython Web Server</h1>
  Hallo!
</body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5) # max 5 concurrent connections

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        print("got a connection from {0}".format(addr))
        request = conn.recv(1024)
        print(request.splitlines()[0]) # header, first line
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(web_page()
)
        conn.close()
    except OSError as e:
        conn.close()
        print('connection closed')
