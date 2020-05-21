# coding:utf-8
from flask import Flask,current_app,redirect,url_for

app = Flask(__name__)
@app.route("/")
def index():
    return "hello flask"
@app.route("/post_only",methods=["post"]) #此处method指定请求方式
def post_only():
    return "psot only page"

@app.route("/hello",methods=["POST"])
def hello():
    return "hello1"

@app.route("/hello",methods=["GET"])
def hello1():
    return "hello2"

## 两个路由对应一个试图函数
@app.route("/hi")
@app.route("/hi1")
def hi():
    return "hei"

@app.route("/login")
def login():
    # 使用url_for的函数，通过试图函数的名字找到试图函数
    url = url_for("index")
    return  redirect(url)
    # return "++++++++++++++start login+++++++++++++++++++"

if __name__ == '__main__':
    # 启动flask程序
    # app.run(host="0.0.0.0",port=5000,debug=True)
    print(app.url_map)  #  查看整个flask的路由信息
    app.run()
