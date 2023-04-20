from flask import Blueprint, render_template, request,url_for, redirect
from .services.create_post import create_post
from .services.update_post import update_post
from ..articles.models import Articles, Authors
from app.extensions.database import db

blueprint = Blueprint('posts', __name__)

@blueprint.get('/posts')
def get_posts():
  slug= request.args.get('slug')
  if slug:
    edited_article = Articles.query.filter_by(slug=slug).first()
    return render_template('posts/new.html',edited_article=edited_article)
  else:
    return render_template('posts/new.html')

@blueprint.post('/posts')
def post_posts():
  title = request.form.get('title')
  
  #check if the title is existing
  is_existing = Articles.query.filter_by(title=title).first()
  if is_existing:
    #update existing article
    update_post(request.form, is_existing)

  else:
    #create new article
    create_post(request.form)
  
  return render_template('posts/new.html')



@blueprint.post('/posts/delete')
def delete_posts():
  id = request.form.get('id')
  #check if the title is existing
  post = Articles.query.filter_by(id=id).first()
  post.delete()
  return redirect (url_for('articles.index'))


