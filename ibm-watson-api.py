import requests
import json

headers = {
    'Content-Type': 'audio/flac',
}

with open('credentials.json') as file:
    credentials = json.loads(file.read())

data = open('C:/Users/lilac/Downloads/NewRecording7.flac', 'rb').read()
url = '{url}/v1/recognize'.format(url=credentials['url'])
response = requests.post(
    url, headers=headers, data=data, auth=('apikey', credentials['apikey']))
print(response.text)
