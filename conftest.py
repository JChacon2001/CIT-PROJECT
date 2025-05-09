import os
import pytest
from app import app,create_app, db
import models
from flask import Flask

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app(config_class=TestConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    return app


# fixtures

# @pytest.fixture
# def test_client():
#     flask_app = create_app()

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as testing_client:
#         # Establish an application context
#         with flask_app.app_context():
#             yield testing_client  

# @pytest.fixture
# def test_client():
#     app = create_app()
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#     app.config['WTF_CSRF_ENABLED'] = False

#     with app.test_client() as testing_client:
#         with app.app_context():
#             db.create_all()
#             yield testing_client
#             db.drop_all()
@pytest.fixture
def test_client():
    return app.test_client(TestConfig)

@pytest.fixture
def test_client2():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:database.db:'
    app.config['WTF_CSRF_ENABLED'] = False


    with app.app_context():  # Ensure app context is active
        db.create_all()

    with app.test_client() as testing_client:
        with app.app_context():  # again during test execution
            yield testing_client

    # with app.app_context():
    #     db.drop_all()
