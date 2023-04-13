def test_login_success(client):
    #login page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_signup_success(client):
    #signup page loads
    response = client.get('/signup')
    assert response.status_code == 200

