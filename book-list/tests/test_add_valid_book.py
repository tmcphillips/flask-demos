import json
import pytest

from app.app import app

new_book = {
	"name": "Frankenstein",
	"price": 7.99,
	"isbn": 12321321312
}

@pytest.fixture
def response(request):
    client = app.test_client()
    return client.post('/books', data=json.dumps(new_book))

# def test_response_status_is_success(response):
#     assert response.status == '200 OK'
#     assert response.status_code == 200

# def test_response_body_is_json(response):
#     assert response.is_json
#     assert response.mimetype == 'application/json' 

# def test_response_header_has_two_keys(response):
#     assert len(response.headers) == 2
#     assert response.headers['Content-Type'] == 'application/json'
#     assert int(response.headers['Content-Length']) > 0
