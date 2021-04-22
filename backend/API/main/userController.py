from flask import request, jsonify, Blueprint
from .userModel import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

user = Blueprint('user', __name__,)

@user.route('/', methods=['GET'])
def home():
    return "<h1>Some weird html here.</h1>"

@user.route('/api/users/all', methods=['GET'])
def get_all_users():
    results = db.session.query(User).all()
    returnResults= []
    for result in results:
        returnResults.append(result.serialize())
    return jsonify(returnResults)

@user.route('/api/users/<id>', methods=['GET'])
def get_by_id(id):
    if id:
        id = str(id)
    else:
        return 'No id provided'

    result = db.session.query(User).get(id)
    return jsonify(result.serialize())

@user.route('/api/users', methods=['POST'])
def create_user():
    if request.data:
        password = request.json["password"]
        username = request.json["username"]
        try:
            newUser = User(username, password)
            db.session.add(newUser)
            db.session.commit()
            return "successfully inserted"
        except Exception:
            return "body is not of user type"
    else:
        return "couldn't insert data"

