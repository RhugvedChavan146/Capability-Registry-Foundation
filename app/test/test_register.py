from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_module():

    response = client.post(
        "/modules",
        json={
            "name": "Resume Parser",
            "description": "Extract resume information",
            "category": "AI",
            "version": "1.0.0",
            "author": "Admin"
        }
    )

    assert response.status_code == 200


def test_duplicate_registration():

    client.post(
        "/modules",
        json={
            "name": "Duplicate Module",
            "description": "Test",
            "category": "AI",
            "version": "1.0.0",
            "author": "Admin"
        }
    )

    response = client.post(
        "/modules",
        json={
            "name": "Duplicate Module",
            "description": "Test",
            "category": "AI",
            "version": "1.0.0",
            "author": "Admin"
        }
    )

    assert response.status_code == 409