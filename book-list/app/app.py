from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 978039400165
    },
    {
        'name': 'The Cat In the Hat',
        'price': 6.99,
        'isbn': 97802371000193
    }
]

@app.route('/books')
def get_books():
    return jsonify({'books': books})
