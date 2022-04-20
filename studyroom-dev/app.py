from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafeform")
def cafeForm():
    return render_template("cafeForm.html")

@app.route("/main", methods=["GET"])
def main_get():
    list = [
            {
                "id": 1,
                "title": "커피바인더리",
                "imgUrl": "../static/images/download.jpg",
                "region": "서울 강남구",
                "createdAt": 1591714800000,
                "updatedAt": 1591714800000
            },
            {
                "id": 2,
                "title": "커피바인더리",
                "imgUrl": "../static/images/download-1.jpg",
                "region": "서울 강남구",
                "createdAt": 1592406000000,
                "updatedAt": 1592406000000
            },
            {
                "id": 3,
                "title": "커피바인더리",
                "imgUrl": "../static/images/download-2.jpg",
                "region": "서울 강남구",
                "createdAt": 1591196400000,
                "updatedAt": 1591196400000
            },
            {
                "id": 4,
                "title": "커피바인더리",
                "imgUrl": "../static/images/download-3.jpg",
                "region": "서울 강남구",
                "createdAt": 1594738800000,
                "updatedAt": 1594738800000
            },
            {
                "id": 5,
                "title": "커피바인더리",
                "imgUrl": "../static/images/download-4.jpg",
                "region": "서울 강남구",
                "createdAt": 1592924400000,
                "updatedAt": 1592924400000
            }
            ]
    return jsonify({'datas': list})

@app.route("/map", methods=["GET"])
def map_get():
    list = [
            {
                "id": "1",
                "name": "스튜디오 르페리",
                "positions": [37.559643, 127.0811217]
            },
            {
                "id": "2",
                "name": "푸쉬커피",
                "positions": [37.5522944, 127.091274]
            },
            {
                "id": "3",
                "name": "안다즈 커피",
                "positions": [37.5503218, 127.0895022]
            },
            {
                "id": "4",
                "name": "카페 러슬",
                "positions": [37.5486102, 127.0855324]
            }
            ]
    return jsonify({'datas': list})

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
