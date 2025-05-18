from flask import current_app
from db import db

def test_database_connection(test_client2):
    with test_client2.application.app_context():
        result = db.session.execute(db.select(1)).scalar()
        assert result == 1
