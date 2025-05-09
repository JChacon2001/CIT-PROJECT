import os
import pytest
from app import app,create_app, db

# fixtures

@pytest.fixture
def test_client():
    return app.test_client()


@pytest.fixture
def app():
    app = create_app()
    app.config.update(TESTING=True,SQLALCHEMY_DATABASE_URI="sqlite:///:memory:")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
        
    
