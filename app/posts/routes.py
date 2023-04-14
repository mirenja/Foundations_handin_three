from flask import Blueprint, render_template

blueprint = Blueprint('posts', __name__)

@blueprint.get('/posts')
def get_posts():
  return render_template('posts/new.html')

@blueprint.post('/posts')
def post_posts():
  return render_template('posts/new.html')