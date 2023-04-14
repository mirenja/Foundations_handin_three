from app.app import create_app
from app.articles.models import Articles
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

article_info = {
  "berlin" : {"author":"Lovelace","title": "Bite into Berlin; A Foodie's Guide to the Best Local Eats","thumbnail":"images/picture.svg" ,"content":"Berlin's food scene is a wild and untamed beast, with flavors that are as bold as the city's vibrant culture. If you're a foodie with a taste for adventure, buckle up and get ready to explore the raw and unfiltered side of Berlin's culinary landscape.Here are some of the most daring and edgy local eats you simply can't miss. Currywurst This classic Berlin street food may seem ordinary, but locals have taken it to the next level with their fiery sauces and wild toppings. Head to Curry 36 or Curry Mitte for a currywurst with a kick, loaded up with everything from jalapeños to bacon bits."},
  "cologne":{"author":"Rosalind","title":"Sights, Scents, and Surprises", "thumbnail": "images/picture1.svg", "content":"Nestled along the Rhine River, the charming city of Cologne is a true gem of western Germany. It's a city that's steeped in history, with an impressive array of landmarks, museums, and cultural sites. But what sets Cologne apart from other German cities is its unmistakable scent – the scent of Cologne water, a fragrant concoction of citrus, lavender, and herbs that has been a signature scent of the city for centuries. In this article, we'll take a closer look at what makes Cologne such a unique and unforgettable destination."},
  "heidelberg": {"author":"Charlotte", "title":"Discovering the Charm and History of Heidelberg", "thumbnail":"images/picture2.svg","content":"Heidelberg, Germany is a charming university town situated on the Neckar River in southwestern Germany. It is known for its picturesque old town, romantic castle ruins, and vibrant student culture. In this travel blog article, I will take you on a virtual tour of Heidelberg and share some of my favorite experiences in the city."}
}

for slug, article in article_info.items():
  
  new_article = Articles(slug = slug, title = article['title'] ,thumbnail = article['thumbnail'], content = article['content'])
  db.session.add(new_article)

db.session.commit()


