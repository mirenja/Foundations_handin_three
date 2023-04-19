from app.articles.models import Articles,Authors

def update_post(form_data,old_article):
  #the old article will be passed in as an argument when the fucntion is called
  title = form_data.get('title')
  content = form_data.get('content')
  thumbnail = form_data.get('thumbnail')

  old_article.title = title
  old_article.content = content
  old_article.thumbnail = thumbnail
  old_article.save()