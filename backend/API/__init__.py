from flask import Flask

from flask_cors import CORS
import os
from .main.userController import db
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()
DB_URL = os.environ['DATABASE_URL']

def create_app(config_object):
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    db.init_app(app)
    from API.main.userController import user
    from API.main.tournamentController import tournament
    app.register_blueprint(user)
    app.register_blueprint(tournament)
    return app


