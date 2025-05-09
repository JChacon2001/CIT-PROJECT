from flask import Flask
from .config import Config

def create_app(config_object=None):
    app = Flask(__name__)

    if config_object:
        app.config.from_object(config_object)

    # OR if you're passing a dictionary:
    # app.config.from_mapping(config_object)

    # Initialize extensions like SQLAlchemy here
    # db.init_app(app)

    return app
