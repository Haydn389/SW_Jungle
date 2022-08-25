from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
from bson import ObjectId
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.almemo2
# http://localhost:5000/
# http://localhost:5000/memo


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def post_article():
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
    id = list(db.articles.find({},{'_id':1}))
    ids=[]
    for k in range(len(id)):
        ids.append(str(id[k]['_id']))

    print(result)
    print(id)
    print(ids)
    # print(ids)
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles':result, 'id':ids})

@app.route('/memo/del', methods=['POST'])
def delete():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    id_receive = request.form['id_give']
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    print(id_receive)
    db.articles.delete_one({'_id': ObjectId(id_receive)})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})

@app.route('/memo/up', methods=['POST'])
def up():
    title_receive = request.form['title_give']  # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분
    id_receive = request.form['id_give']  # 클라이언트로부터 comment를 받는 부분
    print("☆☆☆☆☆☆새로받은값",title_receive,comment_receive,type(id_receive))
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    # print(id_receive)
    db.articles.update_one({'_id': ObjectId(id_receive)},{'$set':{'url': title_receive, 'comment': comment_receive}})
    # db.articles.insert_one({'url': title_receive, 'comment': comment_receive})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})



    


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)