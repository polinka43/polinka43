import json
import requests

HOST = 'httpbin.org'
PATH = '/json'

# connection = http.client.HTTPConnection(HOST)
# connection.request('GET', PATH)
response = requests.get(f'http://{HOST}/{PATH}')

slides = response.json()

slides_ = slides["slideshow"]['slides']
for item in slides_:
    print(item['title'])
