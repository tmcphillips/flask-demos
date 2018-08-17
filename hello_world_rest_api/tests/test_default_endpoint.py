import pytest

from hello_world_rest_api.app import app

@pytest.fixture(scope='module')
def response():
    client = app.test_client()
    return client.get('/')

def test_response_status_code_is_200(response):
    assert response.status_code == 200

def test_response_status_is_200_ok(response):
    assert response.status == '200 OK'

def test_response_body_is_json(response):
    assert response.is_json

def test_response_mimetype_is_json(response):
    assert response.mimetype == 'application/json'

def test_response_header_has_two_keys(response):
    assert len(response.headers) == 2

def test_response_header_has_key_content_type(response):
    assert 'Content-Type' in response.headers

def test_response_header_has_key_content_length(response):
    assert 'Content-Length' in response.headers

def test_response_content_type_is_application_json(response):
    assert response.headers['Content-Type'] == 'application/json'

def test_response_content_length_is_greater_than_zero(response):
    assert int(response.headers['Content-Length']) > 0

def test_response_data_contains_hello_world_message(response):
    assert b'Hello World!' in response.data

def test_response_json_contains_one_property(response):
    assert len(response.get_json()) == 1

def test_response_json_has_key_greeting(response):
    assert 'greeting' in response.get_json()

def test_response_json_greeting_property_is_hello_world(response):
    assert response.get_json()['greeting'] == 'Hello World!'
