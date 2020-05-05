# -*- coding: utf-8 -*
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

class Config(object):
    """配置参数"""
    #sqlalchemy 的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.0.103:12345/flask_db"
    # 设置sqlalchemy自动跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config.from_object(Config)

# 创建sqlalchemy工具对象
db = SQLAlchemy(app)

class Role(db.Model):
    """用户身份"""
    __tablename__ = "t_roles"  #指定数据库的表名字
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    users = db.relationship("User",backref = "user_role")
    def __repr__(self):
        return  "Role object name : %s" % self.name

class User(db.Model):
    """用户表"""
    __tablename__ = "t_users"  #指定数据库的表名字
    id = db.Column(db.Integer,primary_key=True) # 指明主键；整形的主键，默认自增
    name = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    passwd = db.Column(db.String(64))
    role_id = db.Column(db.Integer,db.ForeignKey("t_roles.id"))
    # user_role = db.relationship("Role")



if __name__ == '__main__':
    #清楚数据库中的所有数据，慎用
    db.drop_all()
    #创建所有的表
    db.create_all()
    role1 = Role(name="admin")  #创建对象
    role2 = Role(name="stuff")  # 创建对象
    db.session.add(role1) #session记录任务对象
    db.session.commit() # 提交
    role2 = Role(name="stuff")  # 创建对象
    db.session.add(role2) #session记录任务对象
    db.session.commit() # 提交
    us1 = User(name='wang',email='wang@163.com',passwd='123456',role_id=role1.id)
    us2 = User(name='zhang',email='zhang@189.com',passwd='201512',role_id=role2.id)
    us3 = User(name='chen',email='chen@126.com',passwd='987654',role_id=role2.id)
    us4 = User(name='zhou',email='zhou@163.com',passwd='456789',role_id=role1.id)
    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()

