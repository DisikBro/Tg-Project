import json
import requests


def get_city():
    request = 'https://catalog.api.2gis.com/2.0/region/search?q=Миасс&key=3919965f-bf13-41f1-8905-c1b49996f645'
    response = requests.get(request).json()
    with open('test.json', 'w') as tj:
        json.dump(response, tj)

