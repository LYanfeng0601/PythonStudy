# coding:utf-8
from flask import Flask,make_response,request

app = Flask(__name__)

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    #设置cokkie,默认有效期是临时cookie，浏览器关闭就无效
    resp.set_cookie("Itcast","python")
    resp.set_cookie("Itcast1", "python1",max_age=3600) # 通过max_age设置有效期，单位s
    return resp

@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("Itcast") #获取cookie
    return c

@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("Itcast1") #删除cookie，设置为cookie为过期
    return resp


if __name__ == '__main__':
    app.run(debug=True,port=5001)