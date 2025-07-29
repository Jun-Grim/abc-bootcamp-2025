import json
import requests



url ="https://pyhub.kr/melon/20231204.json"
response = requests.get(url)

# string->object 객체화시키는 작업 : deserialize(역직렬화)
json_string :str = response.text
respones_obj = json.loads(json_string)

for song in respones_obj:
    print(song["곡명"],song["가수"])
    