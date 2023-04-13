from flask import Blueprint, render_template,redirect,url_for,send_file
from .models import Articles

blueprint = Blueprint('Articles', __name__)


@blueprint.route('/')
def index():
    all_articles = Articles.query.all()
    return render_template('articles/index.html', articles = all_articles)

# the article function is a view function in the Articles blueprint,
# blueprint = Blueprint('Articles', __name__),which takes a slug parameter,
# its endpoint is defined as url_for('Articles.article', slug=article.slug)

@blueprint.route('/<slug>')
def article(slug):
  final_article = Articles.query.filter_by(slug=slug).first()
  return render_template('articles/article.html', articles=final_article, slug=slug)