def test_index_success(client):
    #index page loads succesfully
    response = client.get('/')
    assert response.status_code == 200


# def test_article_success(client):
#     #individual article pages load succesfully
#     response = client.get

