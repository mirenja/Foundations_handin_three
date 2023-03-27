from app.extensions.database import db
from datetime import datetime


class Author(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  # article = db.relationship('Article',backref='article', uselist=False, lazy=True)


    
class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(80), unique= True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(260))
    thumbnail = db.Column(db.String(260))
    # author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    # date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # date = db.Column(db.Date,)


