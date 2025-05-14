# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_table():
    response = client.get("/table?name=Willy")
    assert response.status_code == 200
    assert response.json() == {"message": "The table name is Willy"}

def test_create_user():
    response = client.post("/users/", json={
        "username": "alice",
        "email": "alice@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User created"
    assert data["user"]["email"] == "alice@example.com"

def test_update_user():
    # First, create the user
    client.post("/users/", json={
        "username": "bob",
        "email": "bob@example.com"
    })
    # Now update the user
    response = client.put("/users/bob", json={
        "username": "bob",  # must include all required fields
        "email": "newbob@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["user"]["email"] == "newbob@example.com"