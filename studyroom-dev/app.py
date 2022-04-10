from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rhzwl.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():

    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.fans.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


@app.route("/homework", methods=["GET"])
def homework_get():
    fan_list = list(db.fans.find({}, {'_id': False}))
    return jsonify({'fans': fan_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
