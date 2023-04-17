from flask import Blueprint, render_template,redirect,url_for,send_file,request,current_app
from .models import Articles

blueprint = Blueprint('articles', __name__)

@blueprint.route('/run-seed')
def run_seed():
  if not Articles.query.filter_by(slug='Berlin').first():
    import app.scripts.seed
    return 'Database seed completed!'
  else:
    return 'Nothing to run.'

@blueprint.route('/')
def index():
    page_number = request.args.get('page',1, type=int)
    articles_pagination= Articles.query.paginate(page= page_number, per_page = current_app.config['POSTS_PER_PAGE'])


    # all_articles = Articles.query.all()
    return render_template('articles/index.html', articles_pagination = articles_pagination)

# the article function is a view function in the Articles blueprint,
# blueprint = Blueprint('Articles', __name__),which takes a slug parameter,
# its endpoint is defined as url_for('Articles.article', slug=article.slug)

# @blueprint.route('/<slug>')
# def article(slug):
#   final_article = Articles.query.filter_by(slug=slug).first()
#   return render_template('articles/show.html', articles=final_article, slug=slug)