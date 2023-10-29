import requests

response = requests.get('https://httpbin.org/base64/YXVzYmlsZHVuZyBtaXQgenVrdW5mdA==')
print("Serverantwort: {0}".format(response.text))
