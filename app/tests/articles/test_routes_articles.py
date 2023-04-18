from app.articles.models import Articles, Authors

def test_index_success(client):
    #index page loads succesfully
    response = client.get('/')
    assert response.status_code == 200


# def test_article_success(client):
#     #individual article pages load succesfully
#     response = client.get

#its testing the content of the page buit with the test data added
def test_article_renders_article(client):
    #page loads and renders article
    article = Articles(slug="nairobi",title="Bite into nairobi", content="Berlin's food scene is a wild and untamed beast, with flavors that are as bold as the city's vibrant culture.", thumbnail = "images/picture.svg")
    article.save()

    response = client.get('/')

    assert b'nairobi' in response.data