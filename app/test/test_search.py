from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_modules():

    response = client.get("/modules")

    assert response.status_code == 200


def test_search_keyword():

    response = client.get(
        "/modules/search?keyword=Resume"
    )

    assert response.status_code == 200


def test_search_category():

    response = client.get(
        "/modules/search?category=AI"
    )

    assert response.status_code == 200