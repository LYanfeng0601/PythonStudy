#coding:utf-8

from flask import Flask,session

app = Flask(__name__)
app.config["SECRET_KEY"] = "adsadsASDFASFDA"  #使用session，必须适配

@app.route("/login")
def login():
    session["name"] = "python" #设置session
    session["tel"] = "18612345678"
    return "login success"

@app.route("/index")
def index():
    name = session.get("name") #获取session
    return "hello %s" % name

if __name__ == '__main__':
    app.run(debug=True)