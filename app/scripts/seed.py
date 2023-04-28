from app.app import create_app
from app.articles.models import Articles,Authors
from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

article_info = {
  # "berlin" : {"author":"Lovelace","email": "lovelace@gmail.com", "password": "Password","title": "Bite into Berlin; A Foodie's Guide to the Best Local Eats","thumbnail":"images/berlin3.jpg" ,"content":"Berlin's food scene is a wild and untamed beast, with flavors that are as bold as the city's vibrant culture. If you're a foodie with a taste for adventure, buckle up and get ready to explore the raw and unfiltered side of Berlin's culinary landscape.Here are some of the most daring and edgy local eats you simply can't miss. Currywurst This classic Berlin street food may seem ordinary, but locals have taken it to the next level with their fiery sauces and wild toppings. Head to Curry 36 or Curry Mitte for a currywurst with a kick, loaded up with everything from jalapeños to bacon bits."},
  # "cologne":{"author":"Rosalind","email": "rosalind@gmail.com", "password": "Password","title":"Sights, Scents, and Surprises", "thumbnail": "images/berlin4.jpg", "content":"Nestled along the Rhine River, the charming city of Cologne is a true gem of western Germany. It's a city that's steeped in history, with an impressive array of landmarks, museums, and cultural sites. But what sets Cologne apart from other German cities is its unmistakable scent – the scent of Cologne water, a fragrant concoction of citrus, lavender, and herbs that has been a signature scent of the city for centuries. In this article, we'll take a closer look at what makes Cologne such a unique and unforgettable destination."},
  # "heidelberg": {"author":"Charlotte","email": "charlotte@gmail.com", "password": "Password", "title":"Discovering the Charm and History of Heidelberg", "thumbnail":"images/berlin2.jpg","content":"Heidelberg, Germany is a charming university town situated on the Neckar River in southwestern Germany. It is known for its picturesque old town, romantic castle ruins, and vibrant student culture. In this travel blog article, I will take you on a virtual tour of Heidelberg and share some of my favorite experiences in the city."},
  # "ubud": {"author":"jude","email": "jude@gmail.com", "password": "Password", "title":"A Journey to Bali's Cultural Heartland", "thumbnail":"images/ubud.jpg","content":"Ubud, a small town in Bali, is a popular destination for travelers seeking a serene escape from the hustle and bustle of daily life. Known for its lush greenery, traditional arts, and serene atmosphere, Ubud is a must-visit destination for anyone looking to immerse themselves in Balinese culture."}
  "zanzibar": {"author":"Amina","email": "amina@gmail.com", "password": "Password", "title":" The Fascinating Culture of Zanzibar", "thumbnail":"images/zanzibar.jpg","content":"The island's spices are a testament to this cultural melting pot. Zanzibar is often referred to as the Spice Island due to its production of cloves, nutmeg, cinnamon, and black pepper, among others. Walking through the markets, you'll be greeted by the heady aromas of freshly ground spices and exotic fruits."},
  # "amboselli": {"author":"Wafula","email": "wafula@gmail.com", "password": "Password", "title":" The Fascinating Culture of Zanzibar", "thumbnail":"images/amboselli.jpg","content":"But don't let the serene beauty of Amboseli fool you - this park is not for the faint of heart. If you're looking for adventure, you've come to the right place. From heart-pumping game drives to thrilling hot air balloon rides, there's no shortage of excitement to be had in Amboseli."},
  # "venice": {"author":"Tina","email": "tina@gmail.com", "password": "Password", "title":" Venizia", "thumbnail":"images/venice.jpg","content":"The island's spices are a testament to this cultural melting pot. Zanzibar is often referred to as the Spice Island due to its production of cloves, nutmeg, cinnamon, and black pepper, among others. Walking through the markets, you'll be greeted by the heady aromas of freshly ground spices and exotic fruits."},
  # "Rome": {"author":"Peter","email": "peter@gmail.com", "password": "Password", "title":" The Fascinating Culture of Zanzibar", "thumbnail":"images/zanzibar.jpg","content":"The island's spices are a testament to this cultural melting pot. Zanzibar is often referred to as the Spice Island due to its production of cloves, nutmeg, cinnamon, and black pepper, among others. Walking through the markets, you'll be greeted by the heady aromas of freshly ground spices and exotic fruits."},
  # "capadoccia": {"author":"Deniz","email": "deniz@gmail.com", "password": "Password", "title":" The Fascinating Culture of Zanzibar", "thumbnail":"images/capadocia.jpg","content":"The island's spices are a testament to this cultural melting pot. Zanzibar is often referred to as the Spice Island due to its production of cloves, nutmeg, cinnamon, and black pepper, among others. Walking through the markets, you'll be greeted by the heady aromas of freshly ground spices and exotic fruits."},
  # "Marakesh": {"author":"Abdul","email": "abdul@gmail.com", "password": "Password", "title":" The Fascinating Culture of Zanzibar", "thumbnail":"images/marakesh.jpg","content":"The island's spices are a testament to this cultural melting pot. Zanzibar is often referred to as the Spice Island due to its production of cloves, nutmeg, cinnamon, and black pepper, among others. Walking through the markets, you'll be greeted by the heady aromas of freshly ground spices and exotic fruits."}






}
user_info = {
  # "lovelace":{"email": "lovelace@gmail.com", "password": "Password"},
  # "Rosalind":{"email": "rosalind@gmail.com", "password": "Password"},
  # "Charlotte":{"email": "charlotte@gmail.com", "password": "Password"},
  # # "jude":{"email": "jude@gmail.com", "password": "Password"},
  # "Peter":{"email": "peter@gmail.com", "password": "Password"},
  # "Deniz":{"email": "deniz@gmail.com", "password": "Password"},
  # "abdul":{"email": "abdul@gmail.com", "password": "Password"},
  # "Tina":{"email": "tina@gmail.com", "password": "Password"},
  # "wafula":{"email": "wafula@gmail.com", "password": "Password"},
  "Amina":{"email": "amina@gmail.com", "password": "Password"},
}
  
for person,details in user_info.items():
  user = User(fullname=person,email=details['email'],password=generate_password_hash(details['password']))
  db.session.add(user)
  db.session.commit()
  
  author = Authors(user=user)
  db.session.add(author)
  db.session.commit()

for slug, article in article_info.items():


 

  new_article = Articles(slug = slug, title = article['title'] ,thumbnail = article['thumbnail'], content = article['content'], author= author)
  db.session.add(new_article)

db.session.commit()


