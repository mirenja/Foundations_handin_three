from app.articles.models import Articles,Authors
from app.users.models import User
from flask_cors import CORS, cross_origin
from os import environ
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
from flask import jsonify

def create_post(form_data):
    #create a new post
  # post = Articles()
  # post.save
  #get all form data
  name = form_data.get('name')
  city = form_data.get('city')
  title = form_data.get('title')
  content = form_data.get('content')
  thumbnail = form_data.get('thumbnail')

  # find the user by name
  user = User.query.filter_by(fullname=name).first()
  if not user:
    user=User(fullname=name)
    user.save()

  # author = Authors(user=user)
  author = Authors(user_id=user.id)
  author.save()
  # if thumbnail:
  #   print(f"Path to thumbnail: {thumbnail}")
  #   cloudinary.config(cloud_name = environ.get('CLOUD_NAME'), api_key=environ.get('API_KEY'), 
  #   api_secret=environ.get('API_SECRET'))
  #   upload_result = cloudinary.uploader.upload(thumbnail)

  article = Articles(
        slug=city,
        title=title,
        content=content,
        city=city,
        thumbnail=thumbnail,
        author_id=author.id
    )
    
  article.save()

# config = cloudinary.config(secure=True)


# def upload_file(form_data):
#   cloudinary.config(cloud_name = environ.get('CLOUD_NAME'), api_key=environ.get('API_KEY'), 
#     api_secret=environ.get('API_SECRET'))
#   thumbnail = form_data.get('thumbnail')

#   if thumbnail:
#     upload_result = cloudinary.uploader.upload(thumbnail)
#     return jsonify(upload_result)



                                              

  

