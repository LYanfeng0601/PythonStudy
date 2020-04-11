# coding:utf-8
import json
from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/index",methods=["GET"])
def index():
    # #json是字符串
    # data = {
    #     "name": u"python",
    #     "age": 18
    # }
    #data_str = json.dump(data) #将python的字典转换为json字符串
    # print data_str
    # json_str = json.dumps(data)
    # return json_str,200,{"Content-Type":"application/json"}
    # 帮助转换为json数据，并设置响应头application/json
    #return jsonify(data)return jsonify({"name": "annie", "age": 12})
    return jsonify({"name": "annie", "age": 12})
if __name__ == '__main__':
    app.run(debug=True)