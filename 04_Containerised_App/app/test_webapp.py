import os
import sys

# Add the parent directory of the current file to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import pytest
from app import app, model_setup, routes


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage_access(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DNA Analysis" in response.data


def test_log_page_access(client):
    response = client.get("/log_page")
    assert response.status_code == 200
    assert b"Logistic Regression" in response.data


def test_dt_page_access(client):
    response = client.get("/dt_page")
    assert response.status_code == 200
    assert b"Decision Tree" in response.data


def test_rf_page_access(client):
    response = client.get("/rf_page")
    assert response.status_code == 200
    assert b"Random Forest" in response.data
