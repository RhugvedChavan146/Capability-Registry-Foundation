from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_invalid_version():

    response = client.post(
        "/modules",
        json={
            "name": "AI Module",
            "description": "Testing",
            "category": "AI",
            "version": "abc",
            "author": "Admin"
        }
    )

    assert response.status_code == 400


def test_missing_name():

    response = client.post(
        "/modules",
        json={
            "name": "",
            "description": "Testing",
            "category": "AI",
            "version": "1.0.0",
            "author": "Admin"
        }
    )

    assert response.status_code == 400