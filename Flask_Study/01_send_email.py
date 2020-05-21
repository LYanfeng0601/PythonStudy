# coding:utf-8
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
#配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '1104296302@qq.com',
    MAIL_PASSWORD = 'fhpbcxisabrdiief',
)

mail = Mail(app)

@app.route('/')
def index():
 # sender 发送方，recipients 接收方列表
    msg = Message("This is a test ",sender='1104296302@qq.com', recipients=['liyanfeng0601@163.com'])
    #邮件内容
    msg.body = "Flask test mail"
    #发送邮件
    mail.send(msg)
    print "Mail sent"
    return "Sent　Succeed"

if __name__ == "__main__":
    app.run()