import pytest
from cicd import app as flask_app
from cicd import db


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def empty_db(app):
    db.create_all()
    yield db

    # teardown
    db.session.remove()
    db.drop_all()
