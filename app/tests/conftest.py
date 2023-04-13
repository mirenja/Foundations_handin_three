import pytest

from app.app import create_app

@pytest.fixture
def client():
    app =  create_app()

    with app.app_context():
        yield app.test_client()
#within the context of the applicatio do the following.
#yield functions as return but we can still run some code after its done running