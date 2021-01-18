from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/childcare', methods=['GET'])
def childcare_data():
    # 1. DB에서 리뷰 정보 모두 가져오기
    data = list(db.childcare.find({}, {'_id': False}).limit(50))
    return jsonify({'result': 'success', 'data': data})

@app.route('/search/gu', methods=['GET'])
def childcare_data_gu():
    gu_receive = request.args.get('keyword')
    data = list(db.childcare.find({'gu_name': gu_receive}, {'_id': False}))
    return jsonify({'result': 'success', 'data': data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# 1. 다른 어린이집 정보 더 불러오기 - 튜터 1/17(일) 질문
# 2. 어린이집 정보를 드랍박스로 소팅하기 - 일단 검색부터, 드랍박스는 1/17(일) 질문
# 3. 어린이집 링크 달기 - 1/16(토)
# 4. 어린이집 지도 연결하기 -1/16(토)