from flask import Flask, redirect,url_for,render_template,send_file
from . import articles, simple_pages
from app.extensions.database import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config') #where to find config file


    register_extensions(app)
    register_blueprints(app)
    
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(articles.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)



def register_extensions(app: Flask):
    db.init_app(app) #initilize db connection
    migrate.init_app(app, db, compare_type =  True) #if i change the types in my models within the columns, it will allow us create migration instances for it



