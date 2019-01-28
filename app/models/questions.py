from app import db
from datetime import datetime


class Question(db.Model):
    __tablename__ = 'questions'
    id = db. Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text())
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

   