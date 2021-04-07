import flask
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Some weird html here.</h1>"

@app.route('/api/books/all', methods=['GET'])
def getAll():
    return jsonify(books)

# get by id query params way
@app.route('/api/books', methods=['GET'])
def get_by_id1():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'No id provided'
    
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return 'No book found for id '+id


@app.route('/api/books/<id>', methods=['GET'])
def get_by_id2(id):
    if id:
        id = int(id)
    else:
        return 'No id provided'
    
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return 'No book found for id '+str(id)
app.run()