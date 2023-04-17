from app.extensions.database import db
from app.articles.models import Articles,Authors

def test_article_update(client):
    #updates the articles content
    article = Articles(slug="berlin",title="Bite into Berlin", content="Berlin's food scene is a wild and untamed beast, with flavors that are as bold as the city's vibrant culture.", thumbnail = "images/picture.svg")
    db.session.add(article)
    db.session.commit()

    article.title ="A foodies's guide to Berlin"
    article.save()
    print(article.title)

    updated_article = Articles.query.filter_by(slug='berlin').first()
    print(updated_article)
    assert updated_article.title == "A foodies's guide to Berlin"


def test_article_delete(client):
    #delete the specific article

    article = Articles(slug="nairobi",title="Bite into nairobi", content="Berlin's food scene is a wild and untamed beast, with flavors that are as bold as the city's vibrant culture.", thumbnail = "images/picture.svg")
    db.session.add(article)
    db.session.commit()

    article.delete()

    deleted_cookie = Articles.query.filter_by(slug='nairobi').first()
    assert deleted_cookie is None

