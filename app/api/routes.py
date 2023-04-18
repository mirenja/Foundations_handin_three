from flask import Blueprint, jsonify
from .services.serialize_posts import serialize_posts
from ..articles.models import Articles, Authors


blueprint =  Blueprint('api',__name__)

@blueprint.get('/api/v1/posts')
def posts():
    posts = Articles.query.all()
    return jsonify(
        serialize_posts(posts)
    )


#flask converts the json dictionary into JSOn string automatically