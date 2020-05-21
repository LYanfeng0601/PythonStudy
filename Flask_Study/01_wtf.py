#coding:utf-8
from flask import  Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
app.config["SECRET_KEY"] = "ADFADFsdsds"
#定义表单的模型类
class RegisterFormt(FlaskForm):
    """ 自定义模型类"""
    #validators 验证器，DataRequired 保证数据必须填写，并且不能为空
    username = StringField(label=u"用户名",validators=[DataRequired(u"用户名不能为空")])
    passwd = PasswordField(label=u"密码",validators=[DataRequired(u"用户名不能为空")])
    passwd1 = PasswordField(label=u"确认密码",validators=[DataRequired(u"用户名不能为空"),EqualTo("passwd",u"密码不一致")])
    submit = SubmitField(label=u"提交")


@app.route("/register",methods=['GET','POST'])
def register():
    #创建表单对象
    form = RegisterFormt()
    # 如果form中的数据完全满足所有被验证器，validate_on_submit返回真，否则返回假
    if form.validate_on_submit():
        #提取数据
        username = form.username.data
        passwd = form.passwd.data
        print (username,passwd)
        session["uname"] = username

        return redirect(url_for("index"))
    return render_template("register.html",form=form)
@app.route("/index")
def index():
    uname = session.get("uname","guest")
    return "welcome % s idnex page" % uname

if __name__ == '__main__':
    app.run(debug=True)