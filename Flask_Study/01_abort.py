#  coding:utf-8

from flask import  Flask,request,abort,Response

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    if name == "zhangsan" and pwd == "zhangsan":
        pass
    else:
        # 使用abort可以终止函数的执行，并返回前端
        # 1. 传递状态码, 必须是标准的状态码
        abort(404)
        # 2. 传递响应体信息
        # resp = Response("login fail")
        # abort(resp)
    return "login success"

@app.errorhandler(404)
def handle_404_error(err):
    """自定义处理错误方法"""
    # z这个函数的返回值会是前端用户看到的最终结果
    return u"出现了404错误，错误信息：%s" % err



if __name__ == '__main__':
    app.run()
