def test_index_content(client):
    #testing index page content
    response =  client.get('/')

    assert b'Otherwise!!!' in response.data