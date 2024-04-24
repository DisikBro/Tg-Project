import requests

apikey = '3919965f-bf13-41f1-8905-c1b49996f645'

locality = input()
first_request = f'https://catalog.api.2gis.com/2.0/region/search?q={locality}&key={apikey}'
first_response = requests.get(first_request).json()
print(len(first_response))
city_id = first_response['result']['items'][0]['id']
