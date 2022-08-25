from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home():
#    return 'This is Home!'
    return render_template('index.html')

@app.route('/mypage')
def mypage():  
   return 'This is My Page!'


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

# http://localhost:5000/
# http://localhost:5000/mypage