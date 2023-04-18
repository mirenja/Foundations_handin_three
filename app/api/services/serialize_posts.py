#this is the fucntion to return the datasctructure that has all the data currently in the db
def serialize_posts(posts):
    posts_list = []

    for post in posts:
        posts_list.append({
            "id" : post.id,
             "date": post.created_at.strftime('%Y- %m-%d %H:%M:%S'),
            "title":post.title,
            "slug":post.slug,
            "city":post.city,
            "content":post.content,
            "city": post.city,
            # "thumbnail":post.thumbnail,
            "author":post.author.name

        
        })
    return posts_list

