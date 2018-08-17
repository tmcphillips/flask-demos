from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 978039400165
    },
    {
        'name': 'The Cat in the Hat',
        'price': 6.99,
        'isbn': 97802371000193
    }
]

def is_valid_book(book):
    return ('name'  in book and 
            'price' in book and 
            'isbn'  in book)

# GET /books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    request_json = request.get_json()
    if (is_valid_book(request_json)):
        books.insert(0, request_json)
        return 'True'
    else:
        return 'False'

# GET /books/<isbn>
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price'],
                'isbn': book['isbn']
            }
    return jsonify(return_value)