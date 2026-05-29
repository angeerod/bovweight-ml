import json
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_predict_valid(client):
    payload = {"height_cm": 140, "length_cm": 150, "girth_cm": 180}
    res = client.post("/predict", data=json.dumps(payload), content_type="application/json")
    assert res.status_code == 200
    data = res.get_json()
    assert "estimated_weight_kg" in data
    assert data["estimated_weight_kg"] == 450.0


def test_predict_missing_field(client):
    payload = {"height_cm": 140, "length_cm": 150}
    res = client.post("/predict", data=json.dumps(payload), content_type="application/json")
    assert res.status_code == 400


def test_predict_invalid_value(client):
    payload = {"height_cm": -5, "length_cm": 150, "girth_cm": 180}
    res = client.post("/predict", data=json.dumps(payload), content_type="application/json")
    assert res.status_code == 422
