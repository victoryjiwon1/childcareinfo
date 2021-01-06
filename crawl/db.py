import requests
import pprint
from pymongo import MongoClient

# 맛집 데이터는 seoul_matjip 이라는 데이터베이스에 저장하겠습니다.
client = MongoClient('localhost', 27017)
db = client.seoul_matjip

# 서울시 구마다 맛집을 검색해보겠습니다.
seoul_gu = ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구", "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"]

# 네이버 검색 API 신청을 통해 발급받은 아이디와 시크릿 키를 입력합니다.
client_id = "나의 클라이언트 아이디"
client_secret = "나의 시크릿 키"