from flask import Blueprint, jsonify, request
from .services.serialize_posts import serialize_posts
from ..articles.models import Articles, Authors
from os import environ


blueprint =  Blueprint('api',__name__)

@blueprint.get('/api/v1/posts')
def posts():
    if environ.get('API_KEY') == request.headers.get('X-API-KEY'):
        posts = Articles.query.all()
        return jsonify(
        serialize_posts(posts)
    )
    else:
        return jsonify({'error':'invalid API key'}),401

    
    


#flask converts the json dictionary into JSOn string automatically