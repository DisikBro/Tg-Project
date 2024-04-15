import json
import requests

a = []

second_request = ('https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id=32'
                '&q=достопримечательности&key=3919965f-bf13-41f1-8905-c1b49996f645')
second_response = requests.get(second_request).json()
print(second_response)
for i in range(4):
    a.append(second_response['result']['items'][i]['caption'])
print(a)

# requests3 = 'https://catalog.api.2gis.com/3.0/items?rubric_id=112670&region_id=87&key=3919965f-bf13-41f1-8905-c1b49996f645'
# response2 = requests.get(requests3).json()
# with open('test2.json', 'w') as r2:
#     json.dump(response2, r2, indent=3)
