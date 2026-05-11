import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Dados de teste
TEST_USER = {"username": "testuser_pytest", "password": "Senha@123"}

def test_register_success():
    response = client.post("/register", json=TEST_USER)
    assert response.status_code in [201, 400]  # 400 se já existe

def test_register_weak_password():
    response = client.post("/register", json={"username": "user2", "password": "fraca"})
    assert response.status_code == 422

def test_register_no_uppercase():
    response = client.post("/register", json={"username": "user3", "password": "senha@123"})
    assert response.status_code == 422

def test_register_no_special_char():
    response = client.post("/register", json={"username": "user4", "password": "Senha1234"})
    assert response.status_code == 422

def test_login_success():
    client.post("/register", json=TEST_USER)
    response = client.post("/login", data={"username": TEST_USER["username"], "password": TEST_USER["password"]})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

def test_login_wrong_password():
    response = client.post("/login", data={"username": TEST_USER["username"], "password": "Errada@123"})
    assert response.status_code == 401

def test_profile_without_token():
    response = client.get("/profile")
    assert response.status_code == 401

def test_profile_with_token():
    client.post("/register", json=TEST_USER)
    login = client.post("/login", data={"username": TEST_USER["username"], "password": TEST_USER["password"]})
    token = login.json()["access_token"]
    response = client.get("/profile", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_logout_and_profile_blocked():
    client.post("/register", json=TEST_USER)
    login = client.post("/login", data={"username": TEST_USER["username"], "password": TEST_USER["password"]})
    token = login.json()["access_token"]
    client.post("/logout", headers={"Authorization": f"Bearer {token}"})
    response = client.get("/profile", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401

def test_security_headers():
    response = client.get("/")
    assert response.headers.get("x-content-type-options") == "nosniff"
    assert response.headers.get("x-frame-options") == "DENY"
    assert "strict-transport-security" in response.headers