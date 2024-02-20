from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

db= declarative_base()

class FeedbackUsers(db):
    id = db.Column(Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

class Comments(db):
    id = db.Column(Integer, primary_key=True)
    comment = db.Column(db.String(600), nullable=True)
    f_user_id = db.Column(db.Integer, db.ForeignKey(''))




