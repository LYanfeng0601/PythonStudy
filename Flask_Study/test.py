#coding:utf-8
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 随便定义个json字典
dic = {"a": 1, "b": 2, "c": "你好"}


@app.route('/jsonify')
def jsonifys():
    # Content-Type: application/json
    return jsonify(dic)


@app.route('/jsondumps')
def jsondumps():
    # Content-Type: text/html; charset=utf-8
    return json.dumps(dic, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
