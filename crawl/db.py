import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

response = requests.get("http://openapi.seoul.go.kr:8088/7370516d557669633436637346536e/json/ChildCareInfo/1/100/")
result = response.json()
raw_data = result["ChildCareInfo"]["row"]

for data in raw_data:
    print(data['SIGUNNAME'], data['CRNAME'], data['CRADDR'], data['CRCAPAT'])


    doc = {
        'name': data['CRNAME'],
        'gu_name': data['SIGUNNAME'],
        'type': data['CRTYPENAME'],
        'full_count': data['CRCAPAT'],
        'now_count': data['CRCHCNT'],
        'address': data['CRADDR'],
        'map_la': data['LA'],
        'map_lo': data['LO']
    }
    db.childcare.insert_one(doc)
