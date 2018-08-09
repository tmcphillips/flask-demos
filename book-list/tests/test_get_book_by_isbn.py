import pytest

from app.app import app

@pytest.fixture
def client(request):
    return app.test_client()

@pytest.fixture
def response(client):
    return client.get('/books/97802371000193')

@pytest.fixture
def response_json(response):
    return response.get_json()

def test_response_status_is_success(response):
    assert response.status == '200 OK'
    assert response.status_code == 200

def test_response_body_is_json(response):
    assert response.is_json
    assert response.mimetype == 'application/json'

def test_response_header_has_two_keys(response):
    assert len(response.headers) == 2
    assert response.headers['Content-Type'] == 'application/json'
    assert int(response.headers['Content-Length']) > 0

def test_response_json_contains_keys_for_one_book(response_json):
    assert len(response_json) == 3
    assert 'name' in response_json
    assert 'price' in response_json
    assert 'isbn' in response_json

def test_response_json_contains_correct_book_metadata(response_json):
    assert response_json['name'] == 'The Cat in the Hat'
    assert response_json['price'] == 6.99
    assert response_json['isbn'] == 97802371000193

