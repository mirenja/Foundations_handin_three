
from app.extensions.database import db, CRUDMixing
from datetime import datetime


class Authors(db.Model, CRUDMixing):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  email= db.Column(db.String(80))
  password = db.Column(db.String(80))
  articles = db.relationship('Articles',backref='articles', uselist=False, lazy=True)




    
class Articles(db.Model,CRUDMixing):
    id = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(80), unique= True)
    title = db.Column(db.String(80))
    city = db.Column(db.String(80))
    content = db.Column(db.Text())
    thumbnail = db.Column(db.String(80))
    created_at =db.Column(db.DateTime, default=datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
   



