# coding:utf-8
from flask import  Flask,render_template,request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)

#配置数据库
class Config(object):
    """配置参数"""
    #sqlalchemy 的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.0.103:12345/author_book"
    # 设置sqlalchemy自动跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "asdada"
app.config.from_object(Config)
# 创建sqlalchemy工具对象
db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = "t_authors"
    id = db.Column(db.Integer,primary_key=True)
    name =  db.Column(db.String(32),unique=True)
    books = db.relationship("Book",backref="author")
    email = db.Column(db.String(64))
class Book(db.Model):
     __tablename__ = "t_books"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(64), unique=True)
     lead = db.Column(db.String(64), unique=True)
     author_id = db.Column(db.Integer,db.ForeignKey("t_authors.id"))

class AuthorBookForm(FlaskForm):
    """创建表单模型类"""
    author_name = StringField(label=u"作者",validators=[DataRequired(u"作者必填")])
    book_name = StringField(label=u"书籍", validators=[DataRequired(u"书籍必填")])
    submit =SubmitField(label=u"保存")


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        # book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)
@app.route("/delete_book",methods=["POST","GET"])
@app.route("/delete_book", methods=["GET"])
def delete_book():
    """删除数据"""
    # 提取参数
    book_id = request.args.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))
if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au_xi = Author(name='我吃西红柿',email='xihongshi@163.com')
    # au_qian = Author(name='萧潜',email='xiaoqian@126.com')
    # au_san = Author(name='唐家三少',email='sanshao@163.com')
    # db.session.add_all([au_xi,au_qian,au_san])
    # db.session.commit()
    # bk_xi = Book(name='吞噬星空',lead='罗峰',author_id=au_san.id)
    # bk_xi2 = Book(name='寸芒',lead='李杨',author_id=au_xi.id)
    # bk_qian = Book(name='飘渺之旅',lead='李强',author_id=au_san.id)
    # bk_san = Book(name='冰火魔厨',lead='融念冰',author_id=au_xi.id)
    # #把数据提交给用户会话
    # db.session.add_all([bk_xi,bk_xi2,bk_qian,bk_san])
    # db.session.commit()
    app.run(debug=True)

