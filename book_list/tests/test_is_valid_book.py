import pytest

from book_list.app import is_valid_book

@pytest.fixture(scope='session')
def empty_object(): 
    return {}

@pytest.fixture(scope='session')
def complete_book():
    return {
        'name': 'F',
        'price': 6.99,
        'isbn': 1234567890
    }

@pytest.fixture(scope='session')
def book_missing_name():
    return {
        'price': 6.99,
        'isbn': 1234567890
    }

@pytest.fixture(scope='session')
def book_missing_price():
    return {
        'name': 'F',
        'isbn': 1234567890
    }

@pytest.fixture(scope='session')
def book_missing_isbn():
    return {
        'name': 'F',
        'price': 6.99,
    }

def test_complete_book_is_valid(complete_book):
    assert is_valid_book(complete_book)

def test_book_missing_name_is_invalid(book_missing_name):
    assert not is_valid_book(book_missing_name)

def test_book_missing_price_is_invalid(book_missing_price):
    assert not is_valid_book(book_missing_price)

def test_book_missing_isbn_is_invalid(book_missing_isbn):
    assert not is_valid_book(book_missing_isbn)

def test_empty_object_is_invalid(empty_object):
    assert not is_valid_book(empty_object)
