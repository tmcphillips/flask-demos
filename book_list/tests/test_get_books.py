import pytest

from book_list.app import app

@pytest.fixture(scope='module')
def client(request):
    return app.test_client()

@pytest.fixture(scope='module')
def response(client):
    return client.get('/books')

@pytest.fixture(scope='module')
def response_json(response):
    return response.get_json()

@pytest.fixture
def response_books(response_json):
    return response_json['books']

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

def test_response_json_contains_just_books_key(response_json):
    assert len(response_json) == 1
    assert 'books' in response_json

def test_response_contains_two_books(response_books):
    assert len(response_books) == 2

