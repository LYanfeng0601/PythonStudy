# coding:utf-8
from flask import Flask,request
app = Flask(__name__)
# 接口 api
@app.route('/index',methods=['GET','POST'])
def index():
    #request中包含了前端发送过来的所有请求数据
    # request.form 直接提取请求体中表单格式的书库，是个类字典的对象
    # 通过request.form可以直接提取表单中表单格式数据，是一个字典类型
    # 通过get方法只能拿到多个同名参数的第一个
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    name_li= request.form.getlist("name")
    print(name_li)
    print(request.data)
    print(request.args)  #获取参数
    return "hello name=%s,pwd=%s" % (name,pwd)

@app.route("/upload",methods=["GET","POST"])
def upload():
    file_obj = request.files.get("pics")
    if file_obj is None:
        #没有发送文件
        return "文件未返回"
    else:
        # 1. 创建一个文件
        # f = open(u"./南怡仙_医学检验_本科.docx","wb")
        # # 2.向文件中写内容
        #data = file_obj.read()
        # f.write(data)
        # # 3.关闭文件
        # f.close()
        # with open(u"./南怡仙_医学检验_本科.docx","wb") as f:
        #     f.write(data)

        file_obj.save("text.docx")

        #flask 中方法封装了

        return "上传成功"




if __name__ == '__main__':
    app.run(debug=True)