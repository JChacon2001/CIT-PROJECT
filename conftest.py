import os
import pytest
from app import app,create_app, db
import models
from flask import Flask
from routes import html_bp 

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app(config_class=TestConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    return app


@pytest.fixture
def test_client():
    return app.test_client(TestConfig)

@pytest.fixture
def test_client2():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config["SECRET_KEY"] = "supersecret"

    app.register_blueprint(html_bp, url_prefix="/")

    with app.app_context():  
        db.create_all()

    with app.test_client() as testing_client:
        with app.app_context():  
            yield testing_client
