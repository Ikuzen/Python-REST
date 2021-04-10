from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from .main.models import db

def create_app(config_object):

    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ml-specialist-python:ml-addict@localhost:5432/flask'
    db.init_app(app)
    from API.main.controller import simple_page
    app.register_blueprint(simple_page)
    return app


