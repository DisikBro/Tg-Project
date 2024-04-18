import json
import requests

ids = []

# locality = input()
# first_request = f'https://catalog.api.2gis.com/2.0/region/search?q={locality}&key=3919965f-bf13-41f1-8905-c1b49996f645'
# first_response = requests.get(first_request).json()
# print(first_response)
# if first_response['meta']['error']['message'] == 'Results not found':
#     print("Введите действительный город!")

third_requests = 'https://catalog.api.2gis.com/3.0/items?rubric_id=112670&region_id=77&key=3919965f-bf13-41f1-8905-c1b49996f645'
third_response = requests.get(third_requests).json()
for i in range(len(third_response['result']['items'])):
    for j in third_response['result']['items'][i]:
        if j == 'building_name':
            ids.append(third_response['result']['items'][i][j])
print(ids)
# for i in third_response['result']['items']:
#     if i == 'building_name':
#         ids.append(third_response['result']['items'][i])
# print(ids)

#
# with open('test2.json', 'w') as t:
#     json.dump(third_response, t, indent=3)

# print(second_response)


# second_request = ('https://catalog.api.2gis.com/2.0/catalog/rubric/search?region_id=32'
#                 '&q=достопримечательности&key=3919965f-bf13-41f1-8905-c1b49996f645')
# second_response = requests.get(second_request).json()
# print(second_response)
# for i in range(4):
#     a.append(second_response['result']['items'][i]['caption'])
# print(a)

# requests3 = 'https://catalog.api.2gis.com/3.0/items?rubric_id=112670&region_id=87&key=3919965f-bf13-41f1-8905-c1b49996f645'
# response2 = requests.get(requests3).json()
# with open('test2.json', 'w') as r2:
#     json.dump(response2, r2, indent=3)
