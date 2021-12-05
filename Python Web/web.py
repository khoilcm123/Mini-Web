from flask import Flask, flash, render_template, redirect, url_for, request,session

app = Flask(__name__)


# # from flask.helpers import flash
# # from flask.wrappers import Request
# # from werkzeug.wrappers import request
# app = Flask(__name__)
# app.secret_key = "public key"
# app.config['SQlALCHEMY_DATABASE_URI'] = 'sqlite://unsers.sqlite3'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.permanent_session_lifetime = timedelta(minutes=5)
# # a = False

# db = SQLAlchemy(app)

# class user(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     name = db.Column("name", db.string(100))
#     email = db.Column("name", db.string(100))

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

# @app.route('/')
# def hello_world():
#     return "hello web" "<h1> khôi To </h1>"

# @app.route("/<name>") #sau 5000 có chữ gì "http://127.0.0.1:5000/home" thì nó in ra hết
# def user(name):
#     return f"Hello {name}!"

@app.route('/')
def home():
    return render_template("tieu_luan.html") #kết nối đến file index.html

@app.route('/change') 
def change():
    return render_template("tieu_luan2.html")

# @app.route("/admin")
# def admin():
#     # if a:
#     return redirect(url_for("user", name="Admin")) #chuyển hướng đến hàm user phía trên
#------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)