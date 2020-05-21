#coding:utf-8
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
def index():
    data = {
        "name":"lisi",
        "age":20,
        "my_dict":{"city":"lanzhou"},
        "mylist":[1,2,34,445],
        "my_int":0
    }
    return render_template("index.html",**data)

def list_step_2(li):
    """自定义过滤器"""
    return li[::2]
app.add_template_filter(list_step_2,"li2") #注册过滤器


#第二种过滤器定义
@app.template_filter("li3")
def list_step_3(li):
    return li[::3]
if __name__ == '__main__':
    app.run()