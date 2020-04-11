#coding:utf-8

from flask import Flask,session,request

app = Flask(__name__)

@app.route("/index")
def idex():
    print ("index is running")
    return "index"

@app.before_first_request
def handle_before_first_request():
    """第一次请求处理之前被执行"""
    print("handle_before_first_request in sunning")

@app.before_request
def hadle_defore_request():
    """请求之前被执行"""
    print("before_request in running")

@app.after_request
def hadle_after_request(response):
    """每一次处理视图函数后被执行，前提是试图函数没有异常"""
    print("after_request isnb running")
    return response

@app.teardown_request
def hadle_teardown_request(response):
    """没次处理请求完之后被执行，不管是否发生异常,工作在非调试模式下"""
    print("teardown_request is running")
    print (request.path)
    return response
if __name__ == '__main__':
    app.run()