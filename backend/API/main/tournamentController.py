from flask import request, jsonify, Blueprint
from .tournamentModel import Tournament
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

tournament = Blueprint('tournament', __name__,)

@tournament.route('/', methods=['GET'])
def home():
    return "<h1>Some weird html here.</h1>"

@tournament.route('/api/tournaments/all', methods=['GET'])
def get_all_tournaments():
    results = db.session.query(Tournament).all()
    returnResults= []
    for result in results:
        returnResults.append(result.serialize())
    return jsonify(returnResults)

@tournament.route('/api/tournaments/<id>', methods=['GET'])
def get_by_id(id):
    if id:
        id = str(id)
    else:
        return 'No id provided'

    result = db.session.query(Tournament).get(id)
    return jsonify(result.serialize())

@tournament.route('/api/tournaments', methods=['POST'])
def create_tournament():
    if request.data:
        name = request.json["name"]
        size = request.json["size"]
        tournament_type = request.json["tournament_type"]
        organizer_id = request.json["organizer_id"]
        try:
            newTournament = Tournament(name, size, tournament_type, organizer_id)
            db.session.add(newTournament)
            db.session.commit()
            return "successfully inserted"
        except Exception:
            return "b"
        return "couldn't insert data"

