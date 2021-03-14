from flask import Flask,render_template
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


if __name__=="__main__":
    app.run(debug=True)