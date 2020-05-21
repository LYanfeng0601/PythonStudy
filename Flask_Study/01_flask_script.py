#coding:utf-8
from flask import  Flask
from flask_script import Manager #启动命令的管理类
app = Flask(__name__)
# 创建Manager 管理对象
manager = Manager(app)
@app.route("/index")
def index():
    return "index"


if __name__ == '__main__':
    #app.run(debug=True)
    manager.run() #通关管理对象启动flask
