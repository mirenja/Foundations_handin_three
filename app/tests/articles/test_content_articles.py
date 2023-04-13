def test_index_content(client):
    #testing index page content
    response =  client.get('/')

    assert b'Travel Blog' in response.data