import pytest
import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    """Test that the root endpoint returns 'Hello, World!' with a 200 status code"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello, World!' in rv.data


def test_404_page(client):
    """Test that accessing a non-existent page returns a 404"""
    rv = client.get('/nonexistent')
    assert rv.status_code == 404
