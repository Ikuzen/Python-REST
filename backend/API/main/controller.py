import flask
import json
from flask import request, jsonify, Blueprint
from .models import Users, db
from sqlalchemy import insert

simple_page = Blueprint('simple_page', __name__,)

@simple_page.route('/', methods=['GET'])
def home():
    return "<h1>Some weird html here.</h1>"

@simple_page.route('/api/users/all', methods=['GET'])
def get_all_users():
    results = db.session.query(Users).all()
    returnResults= []
    for result in results:
        returnResults.append(result.serialize())
    return jsonify(returnResults)

# get by id path variable way
@simple_page.route('/api/users/<id>', methods=['GET'])
def get_by_id(id):
    if id:
        id = str(id)
    else:
        return 'No id provided'

    result = db.session.query(Users).get(id)
    return jsonify(result.serialize())

@simple_page.route('/api/users', methods=['POST'])
def create_user():
    if request.data:
        password = request.json["password"]
        username = request.json["username"]
        try:
            newUser = Users(username, password)
            db.session.add(newUser)
            db.session.commit()
            return "successfully inserted"
        except Exception:
            print(Exception)
            return "body is not of user type"
    else:
        return "couldn't insert data"

