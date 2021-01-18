import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


####  childcare 콜렉션 삭제
db.childcare.drop()

# start_idx = 1
# end_idx = 1000
# list_total_count =  9105
#
#
# response = requests.get(
#     "http://openapi.seoul.go.kr:8088/7370516d557669633436637346536e/json/ChildCareInfo/" + start_idx + "/" + end_idx + "/")

# (1,1000), (1001, 2000), (2001, 3000), (3001. 4000), (4001, 5000), (5001, 6000) ....
#
# + 1000
# + 1000
#
# end_idx > 9105
#
# for :
#     start_idx += 1000
#     end_idx +=1000
#
#     start_idx = i * 1000 + 1
#     end_idx = (i+1) * 1000 + 1
#
# for (let i = 0; i < list_total_count; i++){
#
#     start_idx = i * 1000 + 1
#     end_idx = (i+1) * 1000 + 1
#
# response = requests.get(
#     "http://openapi.seoul.go.kr:8088/7370516d557669633436637346536e/json/ChildCareInfo/" + start_idx + "/" + end_idx + "/")
# }


# response = requests.get(
#     "http://openapi.seoul.go.kr:8088/7370516d557669633436637346536e/json/ChildCareInfo/" + start_idx + "/" + end_idx + "/")



def get_total_count():
    response_cnt = requests.get(
        "http://openapi.seoul.go.kr:8088/7370516d557669633436637346536e/json/ChildCareInfo/1/2/")
    result_cnt = response_cnt.json()
    list_total_count = result_cnt["ChildCareInfo"]["list_total_count"]
    # list_total_count = 9105

    count = int(list_total_count / 1000)
    if list_total_count % 1000 != 0:
        count += 1

    return count

cnt = get_total_count()
#cnt = 10

# 0 ~ 10
for i in range(cnt):
    start_idx = i * 1000 + 1
    end_idx = (i + 1) * 1000

    print(start_idx, end_idx)

    response = requests.get(
        "http://openapi.seoul.go.kr:8088/7370516d557669633436637346536e/json/ChildCareInfo/" + str(start_idx) + "/" + str(end_idx) + "/")

    result = response.json()
    raw_data = result["ChildCareInfo"]["row"]

    for data in raw_data:
        # print(data['SIGUNNAME'], data['CRNAME'], data['CRADDR'], data['CRCAPAT'])

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
