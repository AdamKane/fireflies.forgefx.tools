from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"app": "fireflies.forgefx.tools", "version": "v2024.09.02-01"}

def test_say_hello():
    response = client.get("/hello/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello John"}

@patch('app.fireflies.get_user_count')
def test_get_user_count(mock_get_user_count):
    mock_get_user_count.return_value = 5
    response = client.get("/user_count")
    assert response.status_code == 200
    assert response.json() == {"user_count": 5}
