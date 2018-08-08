import pytest

from app.app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        print("running teardown")

    request.addfinalizer(teardown)

    return test_client

def test_that_passes(client):
    assert True
 
def test_dummmy(client):
    response = client.get('/')
    assert b'Hello World!' in response.data