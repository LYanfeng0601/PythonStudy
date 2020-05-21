# coding:utf-8
from flask import Flask
from order import app_order
from cart import app_cart

app = Flask(__name__)
app.register_blueprint(app_order,url_prefix="/test") #http://127.0.0.1:5052/test/order
app.register_blueprint(app_cart,url_prefix="/cart")
# app.route("/order")(order)
app.logger.error("**************start((((((((((((((((((((((")
@app.route("/")
def index():
    return "index page"

if __name__ == '__main__':
    print (app.url_map)
    app.run(port=5052,debug=True)
