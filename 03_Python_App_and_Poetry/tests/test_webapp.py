# tests/test_webapp.py

import pytest
from flask import url_for
from your_app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage_access(client):
    response = client.get("/")
    assert response.status_code == 200


def test_feature_importance_display(client):
    response = client.get("/")
    assert b"Feature Importance" in response.data


def test_roc_curve_display(client):
    response = client.get("/")
    assert b"ROC Curve" in response.data


def test_model_assessment_text(client):
    response = client.get("/")
    assert b"This is a weak model" in response.data


def test_image_loading(client):
    with app.test_request_context():
        image_url = url_for(
            "static", filename="ROC_curve_for_random_forest_classifier.png"
        )
    response = client.get(image_url)
    assert response.status_code == 200
