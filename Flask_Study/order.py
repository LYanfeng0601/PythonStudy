# coding:utf-8
from flask import Blueprint

#创建蓝图对象
app_order = Blueprint("app_order",__name__)

@app_order.route("/order")
def order():
    return "order"

@app_order.route("/post_order")
def post_order():
    return "post_order"