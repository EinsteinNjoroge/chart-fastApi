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
