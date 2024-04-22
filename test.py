import json
import requests
import urllib

ids = []
info = []





# third_requests = 'https://catalog.api.2gis.com/3.0/items?rubric_id=112670&region_id=87&key=3919965f-bf13-41f1-8905-c1b49996f645'
# third_response = requests.get(third_requests).json()
# ids.append(third_response)
# print(ids[0])
# print(third_response)
# ids.append(third_response)
# print(ids)
# print(third_response)
# for i in range(len(third_response['result']['items'])):
#     for j in third_response['result']['items'][i]:
#         if j == 'building_name':
#             ids.append(third_response['result']['items'][i][j])
# a = input()
# for j in range(len(third_response['result']['items'])):
#     for k in ids[0]['result']['items'][j]:
#         if k == 'building_name':
#             if a.lower() == ids[0]['result']['items'][j][k].lower():
#                 info.append(ids[0]['result']['items'][j])
# print(info)
# for i in info:
#     print(i['address_name'], i['building_name'], i['full_name'], i['purpose_name'], sep='\n')
