from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\Users\gustu\Music\login\start\database\user.db'
db = SQLAlchemy(app)

class contoh (db.Model):
    id = db.Column(db.Integer,primary_key=True)