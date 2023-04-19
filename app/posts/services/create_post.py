from app.articles.models import Articles,Authors

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
 
  author = Authors(name=name)
  author.save()

  article = Articles(
        slug=city,
        title=title,
        content=content,
        city=city,
        thumbnail=thumbnail,
        author_id=author.id
    )
    
  article.save()

  

