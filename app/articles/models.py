
from app.extensions.database import db, CRUDMixing
from datetime import datetime



class Authors(db.Model, CRUDMixing):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  articles = db.relationship('Articles',backref='author', uselist=False, lazy=True)




    
class Articles(db.Model,CRUDMixing):
    id = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(80), unique= True)
    title = db.Column(db.String(80))
    city = db.Column(db.String(80))
    content = db.Column(db.Text())
    thumbnail = db.Column(db.String(80))
    created_at =db.Column(db.DateTime, default=datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

# class ArticlesAuthor(db.model, CRUDMixing):
#    authors_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

   



