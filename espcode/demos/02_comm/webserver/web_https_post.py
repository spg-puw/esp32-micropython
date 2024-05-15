import requests

url = 'https://httpbin.org/anything?somequeryparameter=somevalue'
jsonData = {'somekey': 'somevalue'}

result = requests.post(url, json = jsonData)

print(result.text)
