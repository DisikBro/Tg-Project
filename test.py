import json
import requests

# request = 'https://catalog.api.2gis.com/2.0/region/search?q=Миасс&key=3919965f-bf13-41f1-8905-c1b49996f645'
# response = requests.get(request).json()
# print(response)
# city_id = response['result']['items'][0]['id']
request2 = 'https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id=87&q=достопримечательности&key=3919965f-bf13-41f1-8905-c1b49996f645'
response2 = requests.get(request2).json()
ai = response2['result']['items'][0]['alias']
print(ai)
# requests3 = 'https://catalog.api.2gis.com/3.0/items?rubric_id=112670&region_id=87&key=3919965f-bf13-41f1-8905-c1b49996f645'
# response2 = requests.get(requests3).json()
# with open('test.json', 'w') as r2:
#     json.dump(response2, r2, indent=3)
