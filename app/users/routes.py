from flask import Blueprint, render_template, request, url_for,redirect
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from .services.gmail import get_gmail_service

blueprint = Blueprint('users', __name__)

@blueprint.get('/register')
def get_register():
  return render_template('users/register.html')

@blueprint.post('/register')
def post_register():
  try:

    if request.form.get('password') != request.form.get('password_confirmation'):
      raise Exception('The password confirmation must match the password.')
    elif User.query.filter_by(email=request.form.get('email')).first():
      raise Exception('The email address is already registered.')
    elif len(request.form.get('password')) <= 5 :
      raise Exception('Password is too short!')
    
    user = User(
      fullname = request.form.get('fullname'),
      email = request.form.get('email'),
      password= generate_password_hash(request.form.get('password'))
    )
  
    
    
    # perform user verification
    email = request.form.get('email')
    service = get_gmail_service()
    message = {
      'to' :email,
      'subject':'Verify your journals account',
      'body':'Please click the link to verify your account: <a href="url_for{{articles.index}}">Verify</a>',
      'contentType': 'text/html',

    }
    user.save()
     # Send verification email
    service.users().messages().send(userId='me', body=message).execute()

    login_user(user)
    return redirect(url_for('articles.index'))
  except Exception as error_message:
    error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'

    return render_template ('users/register.html', error=error)

@blueprint.get('/login')
def get_login():
  return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
  try:
    user = User.query.filter_by(email=request.form.get('email')).first()
    if not user:
      raise Exception('No user with that email address was found')
    elif not check_password_hash(user.password, request.form.get('password')):
      raise Exception('The password does not appear to be correct.')
    login_user(user)
    return redirect(url_for('articles.index'))

  except Exception as error_message:
    error = error_message or 'An eooro occured while logging in.Please verify your email and password '
  return render_template ('users/login.html', error=error)

  # ###########################################
@blueprint.post('/register/delete')
def delete_user():
  fullname = request.form.get('fullname')
  email = request.form.get('email')
  #check if the email is existing
  user = User.query.filter_by(email=request.form.get('email')).first()
  if user:
    user.delete()
    
  return redirect (url_for('users.register'))




# ###########################################
@blueprint.get('/logout')
def logout():
  logout_user()
  return redirect(url_for('users.get_login'))





