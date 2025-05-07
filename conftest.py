import os
import pytest
from app import app

# fixtures

@pytest.fixture
def test_client():
    return app.test_client()