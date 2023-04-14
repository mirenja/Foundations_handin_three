from flask import Blueprint, render_template, request
from .services.create_post import create_post


blueprint = Blueprint('posts', __name__)

@blueprint.get('/posts')
def get_posts():
  return render_template('posts/new.html')

@blueprint.post('/posts')
def post_posts():
  create_post(request.form)
  
  return render_template('posts/new.html')