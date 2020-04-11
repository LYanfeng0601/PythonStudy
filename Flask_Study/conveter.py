# coding:utf-8
from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 转换器
# @app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")  # 默认字符串规则；除了/字符
def goods_detail(goods_id):
    return "goods_detail %s" % goods_id


# 1.定义自己的转换器
class ReqexConverter(BaseConverter):
    """"""

    def __init__(self, url_map, reqex):
        # 调用父类的初始化构造方法
        super(ReqexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象属性中，flask会使用这个属性来进行路由的匹配
        self.regex = reqex

    # def to_python(self, value):  # 实际转换器逻辑处理
    #     pass

    def to_url(self, value):  #
        pass


# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = ReqexConverter


@app.route("/send/<re(r'1[345678]\d{9}'):mobile>")
def send_sms(mobile):
    return "send sms to %s" % mobile


if __name__ == '__main__':
    # 启动flask程序
    # app.run(host="0.0.0.0",port=5000,debug=True)
    print(app.url_map)  # 查看整个flask的路由信息
    app.run()
