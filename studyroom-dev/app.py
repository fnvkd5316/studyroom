from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rhzwl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafeform")
def cafeForm():
    return render_template("cafeForm.html")

@app.route("/cafeform", methods=["POST"])
def saveCafeData():

# 카페 이미지
# 카페 이미지 저장 구현은 메인화면에 띄우는것 까지하고!

# 카페 정보
    cafeList = list(db.cafe_test.find({}, {'_id': False}))

    id   = len(cafeList) + 1 #카페 번호
    name = request.form['name'] #카페 이름
    desc = request.form['desc'] #카페 설명

# 주소
    addressInfo      = request.form['addressInfo']      # 도로명주소
    jibunAddressInfo = request.form['jibunAddressInfo'] # 지번주소
    sidoInfo         = request.form['sidoInfo']         # 서울 **시 안붙임**
    sigunguInfo      = request.form['sigunguInfo']      # 금천구
    bname2Info       = request.form['bname2Info']       # 가산동
    detailAddrInfo   = request.form['detailAddrInfo']   # User가 적어준 상세주소
    zonecodeInfo     = request.form['zonecodeInfo']     # 우편번호

# 주소의 위도, 경도
    latitude  = request.form['latitude']  # 위도
    longitude = request.form['longitude'] # 경도

# 생성된 날짜정보 넣기.

    doc = {
            "id":   id,
            "name": name,
            "desc": desc,
            "addressInfo": addressInfo,
            "jibunAddressInfo": jibunAddressInfo,
            "sidoInfo": sidoInfo,
            "sigunguInfo": sigunguInfo,
            "bname2Info": bname2Info,
            "detailAddrInfo": detailAddrInfo,
            "zonecodeInfo": zonecodeInfo,
            "latitude": latitude,
            "longitude": longitude
    }

    db.cafe_test.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})

@app.route("/main", methods=["GET"])
def main_get():
    cafes = list(db.cafe_test.find({}, {'_id': False}))
    cafeList = []

    for cafe in cafes:
        id = cafe['id']
        region = cafe['sidoInfo'] + ' ' + cafe['sigunguInfo']

        doc = {
                'id': id,
                'name': cafe['name'],
                'imgUrl': '',
                'region': region
        }

        cafeList.append(doc)

    # list = [
    #         {
    #             "id": 1,
    #             "name": "커피바인더리",
    #             "imgUrl": "../static/images/download.jpg",
    #             "region": "서울 강남구",
    #             "createdAt": 1591714800000,
    #             "updatedAt": 1591714800000
    #         },

    return jsonify({'datas': cafeList})

@app.route("/map", methods=["GET"])
def map_get():
    cafes = list(db.cafe_test.find({}, {'_id': False}))
    cafeList = []

    for cafe in cafes:
        doc = {
                "id": cafe['id'],
                "name": cafe['name'],
                "positions": [cafe['latitude'], cafe['longitude']]
        }

        cafeList.append(doc)

    # list = [
    #         {
    #             "id": "1",
    #             "name": "스튜디오 르페리",
    #             "positions": [37.559643, 127.0811217]
    #         }
    #         ]
    return jsonify({'datas': cafeList})

@app.route("/login")
def login_form():
    return render_template("login.html")

@app.route("/login/check", methods=["POST"])
def login_check():
    #유저 아이디 정보 받기
    #비밀번호 받기
    #db로 정보 검색
    #아이디, 비밀번호 대조
    #같으면 메인 홈페이지 띄우기

    return render_template("index.html")


@app.route("/signup")
def signup_form():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
