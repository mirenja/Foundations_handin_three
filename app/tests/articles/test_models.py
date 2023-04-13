from app.extensions.database import db
from app.articles.models import Articles

def test_article_update(client):
    #updates the articles content
    article = Articles(title="Bite into Berlin", content="Berlin's food scene is a wild and untamed beast, with flavors that are as bold as the city's vibrant culture.", thumbnail = "mages/picture.svg")
    db.session.add(article)
    db.session.commit()

    article.title ="A foodies's guide to Berlin"
    article.save()

    updated_title = article.query.filter_by(city='berlin').first()
    assert updated_title == "A foodies's guide to Berlin"