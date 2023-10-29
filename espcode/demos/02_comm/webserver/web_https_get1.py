import socket
import ssl

s = socket.socket()
ai = socket.getaddrinfo("www.spengergasse.at", 443)
print("Address infos:", ai)
addr = ai[0][-1]
print("Connect address:", addr)
s.connect(addr)
s = ssl.wrap_socket(s)
s.write(b"GET / HTTP/1.1\r\n")
s.write(b"Host: www.spengergasse.at\r\n")
s.write(b"Connection: close\r\n")
s.write(b"\r\n\r\n")
print(s.read(4096))
s.close()
