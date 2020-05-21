# coding:utf-8
from flask import Flask,current_app
#  创建flask的应用对象
# __name__ 表示当前模块名字
# 模块名，flask以这个模块所在目录为总目录，默认这个目录中的static为静态目录。template为模块目录
app = Flask(__name__,
            static_url_path="/python", # 访问静态文件的url前缀  默认值是static
            static_folder="static", # 访问静态文件的目录
            template_folder="template")  # 访问模板文件的目录
# 配置参数的使用方式
# 1.使用配置文件
#app.config.from_pyfile("config.cfg")

# 2.c从对象中获取配置文件
class Config(object):
    DEBUG = False
    TEST = "A"
app.config.from_object(Config)

# 3.直接操作config字典
# app.config["DEBUG"] = True

@app.route("/")
def index():
    """定义视图函数"""
    # 读取配置参数
    # 1.直接从全局app的config字典中取值
    print (app.config.get("TEST"))
    # 通过current_app获取参数
    print(current_app.config.get("TEST"))
    return "hello flask"

if __name__ == '__main__':
    # 启动flask程序
    # app.run(host="0.0.0.0",port=5000,debug=True)
    app.run()
