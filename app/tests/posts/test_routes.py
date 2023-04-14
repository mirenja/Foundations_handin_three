def test_get_posts_renders(client):
  # Page loads and renders new.html
  response = client.get('/posts')
  assert b'Your Post:' in response.data
