import requests

response = requests.get('http://httpbin.org/base64/YXVzYmlsZHVuZyBtaXQgenVrdW5mdA==')
print("Serverantwort: {0}".format(response.text))
