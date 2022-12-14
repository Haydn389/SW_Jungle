from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기

# http://localhost:5000/
# http://localhost:5000/memo

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.almemo2  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.

# db.test.insert_one({'name':'bobby','age':21})
@app.route('/')
def home():
    return render_template('index.html')

# print("hello")

@app.route('/add', methods=['POST'])
def post_article():
    print("hello")
    # 1. 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give']  # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분
    print(title_receive,comment_receive)
    article = {'url': title_receive, 'comment': comment_receive}

    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)

    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)