# coding:utf-8
from flask import Flask,request,make_response

app = Flask(__name__)

@app.route("/index",methods=["GET"])
def index():
    # 使用元组，返回自定义信息
    #return "hello world",400,[("city","lanzhou")]
    #return "hello world", "666 city status", {"name":"liyanfeng","pwd":"lisi"}  # 状态码都可以指定
    #使用make_response来构造信息
    resp = make_response("index page 2")
    resp.status = "999 hello"
    resp.headers["city"] = "sz"
    return resp

if __name__ == '__main__':
    app.run()