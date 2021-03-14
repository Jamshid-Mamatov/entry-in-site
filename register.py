from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///user_database.db"
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    username=db.Column(db.String(100),unique=True)
    password=db.Column(db.Integer)
    first_name=db.Column(db.String(100))
    last_name=db.Column(db.String(100))

@app.route("/")
def home():
    content="home site"
    return render_template("home.html",content=content)


@app.route("/signup")
def sign_up():
    content="Sign Up"
    position="get_signup"
    return render_template("entry.html",content=content,position=position)

@app.route("/get_signup",methods=["POST"])
def get_sign_up():
    content="register"
    r=request.form
    get_email=r.get("email")
    get_username=r.get("username")
    get_password=r.get("password")
    get_first_name=r.get("first_name")
    get_last_name=r.get("last_name")

    user=User(email=get_email,username=get_username,password=get_password,first_name=get_first_name,last_name=get_last_name)

    db.session.add(user)
    db.session.commit()
    return "ok"


if __name__=="__main__":
    app.run(debug=True)