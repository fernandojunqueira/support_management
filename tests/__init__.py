import pytest
from flaskr import app
from flaskr.app import create_app


@pytest.fixture(scope='module')
def app():
    """Instance of Main flask app"""
    app = create_app()
    with app.app_context():
        yield app