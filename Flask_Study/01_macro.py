# coding: utf- 8
from flask import  Flask,render_template,flash

flag = True
app = Flask(__name__)
app.config["SECRET_KEY"] = "ADFADFsdsds"
@app.route("/index")
def index():
    if flag:
        flash("hello1")
        flash("hello2")
        flash("hello3")
        global flag
        flag = False
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True,port=5001)