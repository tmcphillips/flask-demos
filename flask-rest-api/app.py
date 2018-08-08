from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'greeting': 'Hello World!'})

app.run(port=5000)