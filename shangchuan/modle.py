from exts import db
from datetime import datetime

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    telephone = db.Column(db.String(20), nullable = False)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)

class Article(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    picture_path = db.Column(db.String(100), nullable = True)
    content = db.Column(db.Text, nullable = True)
    create_time = db.Column(db.DateTime, default = datetime.now)