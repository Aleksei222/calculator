from db import db
from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    token = db.relationship('Token', cascade='all, delete')

    def __init__(self, username, password):
        self.login = username
        self.password = password

    def __repr__(self):
        return f'<User id = {self.id}, login = {self.login}, hash = {self.password}>'
class Token(db.Model):
    __tablename__ = 'tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(120))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.Date)

    def __init__(self, token, user, date):
        self.token = token
        self.date = date
        self.user = user
    
    def __repr__(self):
        return f'<Token {self.token}>'
    