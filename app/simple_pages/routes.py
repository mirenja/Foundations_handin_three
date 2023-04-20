from flask import Blueprint, render_template

blueprint = Blueprint('Simple_pages', __name__)


# @blueprint.route('/login')
# def login():
  
  
#   return render_template('simple_pages/login.html') 

@blueprint.route('/signup')
def signup():
  
  
  return render_template('simple_pages/signUp.html') 