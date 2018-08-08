import pytest

from app.app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        print("running teardown")

    request.addfinalizer(teardown)

    return test_client
 
def test_response_contains_hello_world_message(client):
    response = client.get('/')
    assert b'Hello World!' in response.data

def test_response_json_contains_one_key(client):
    response_json = client.get('/').get_json()
    assert len(response_json.keys()) == 1

def test_only_key_in_response_json_is_greeting(client):
    response_json = client.get('/').get_json()
    assert 'greeting' in response_json.keys() 

def test_value_of_response_json_greeting_property_is_hello_world(client):
    response_json = client.get('/').get_json()
    assert response_json['greeting'] == 'Hello World!'