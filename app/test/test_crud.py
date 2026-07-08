from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_module():

    response = client.post(
        "/modules",
        json={
            "name": "CRUD Module",
            "description": "CRUD Testing",
            "category": "Testing",
            "version": "1.0.0",
            "author": "Admin"
        }
    )

    assert response.status_code == 200


def test_read_modules():

    response = client.get("/modules")

    assert response.status_code == 200


def test_delete_module():

    response = client.delete("/modules/1")

    assert response.status_code in [200, 404]