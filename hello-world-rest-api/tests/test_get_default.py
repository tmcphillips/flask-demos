import pytest

from app.hello_world import app

@pytest.fixture
def client(request):
    return app.test_client()

def test_response_status_code_is_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_response_status_is_200_ok(client):
    response = client.get('/')
    assert response.status == '200 OK'

def test_response_body_is_json(client):
    response = client.get('/')
    assert response.is_json

def test_response_mimetype_is_json(client):
    response = client.get('/')
    assert response.mimetype == 'application/json'

def test_response_header_has_two_keys(client):
    response = client.get('/')
    assert len(response.headers) == 2

def test_response_header_has_key_content_type(client):
    response = client.get('/')
    assert 'Content-Type' in response.headers

def test_response_content_type_is_application_json(client):
    response = client.get('/')
    assert response.headers['Content-Type'] == 'application/json'

def test_response_content_length_is_greater_than_zero(client):
    response = client.get('/')
    assert int(response.headers['Content-Length']) > 0

def test_response_header_has_key_content_length(client):
    response = client.get('/')
    assert 'Content-Length' in response.headers

def test_response_contains_hello_world_message(client):
    response = client.get('/')
    assert b'Hello World!' in response.data

def test_response_json_contains_one_key(client):
    response_json = client.get('/').get_json()
    assert len(response_json) == 1

def test_response_json_has_key_greeting(client):
    response_json = client.get('/').get_json()
    assert 'greeting' in response_json 

def test_value_of_response_json_greeting_property_is_hello_world(client):
    response_json = client.get('/').get_json()
    assert response_json['greeting'] == 'Hello World!'