import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Welcome to DevOps Demo App!"
    assert "hostname" in data
    assert "version" in data

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_ready(client):
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ready"

def test_info(client):
    response = client.get("/info")
    assert response.status_code == 200
    data = response.get_json()
    assert data["app"] == "devops-demo"
    assert "version" in data
