from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_fetch_chart_data():
    response = client.get("/chart-data")
    response_data = response.json()

    assert response.status_code == 200
    assert 'chart_data' in response_data
    assert 'industries' in response_data


def test_fetch_comments():
    response = client.get("/comments")
    assert response.status_code == 200


def test_create_new_comment():
    response = client.post(
        "/comments",
        json={
            "username": "foobar",
            "message": "Foo Bar",
            "year": "2014",
            "industry": "Finance"
        },
    )
    response_data = response.json()

    assert response.status_code == 201
    assert response_data['message'] == 'Comment created'
    assert response_data['success'] is True


def test_create_new_comment_with_non_existent_industry():
    response = client.post(
        "/comments",
        json={
            "username": "foobar",
            "message": "Foo Bar",
            "year": "2014",
            "industry": "NON-EXISTENT INDUSTRY"
        },
    )
    response_data = response.json()

    assert response.status_code == 400
    assert response_data['success'] is False
