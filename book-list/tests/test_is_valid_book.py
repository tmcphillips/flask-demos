import pytest

from app.app import is_valid_book

empty_object = {}

complete_book = {
    'name': 'F',
    'price': 6.99,
    'isbn': 1234567890
}

book_missing_name = {
    'price': 6.99,
    'isbn': 1234567890
}

book_missing_price = {
    'name': 'F',
    'isbn': 1234567890
}

book_missing_isbn = {
    'name': 'F',
    'price': 6.99,
}

def test_complete_book_is_valid():
    assert is_valid_book(complete_book)

def test_book_missing_name_is_invalid():
    assert not is_valid_book(book_missing_name)

def test_book_missing_price_is_invalid():
    assert not is_valid_book(book_missing_price)

def test_book_missing_isbn_is_invalid():
    assert not is_valid_book(book_missing_isbn)

def test_empty_object_is_invalid():
    assert not is_valid_book(empty_object)
