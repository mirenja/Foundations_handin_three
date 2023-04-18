from flask import Blueprint, jsonify


blueprint =  Blueprint('api',__name__)

@blueprint.get('/api/v1/posts')
def posts():
    return jsonify({
        "data":"Hello"
    })