import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_valid_profile(client):
    response = client.post(
        "/profile",
        json={"display_name": "Shrejal"}
    )
    assert response.status_code == 200
    assert response.json["display_name"] == "Shrejal"


def test_invalid_input_type(client):
    response = client.post(
        "/profile",
        json={"display_name": 123}
    )
    assert response.status_code == 400


def test_oversized_display_name(client):
    response = client.post(
        "/profile",
        json={"display_name": "A" * 81}
    )
    assert response.status_code == 400


def test_missing_display_name(client):
    response = client.post("/profile", json={})
    assert response.status_code == 400


def test_empty_display_name(client):
    response = client.post(
        "/profile",
        json={"display_name": "   "}
    )
    assert response.status_code == 400