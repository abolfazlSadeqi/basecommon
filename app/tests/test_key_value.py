from fastapi.testclient import TestClient

from app.api.endpoints.key_value import get_db
from app.main import app
from app.db.session import SessionLocal, Base, engine
from app.models.key_value import KeyValue

client = TestClient(app)


def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_create_key_value():
    response = client.post("/key_value/", json={"key": "test", "value": "test_value", "title": "test_title"})
    assert response.status_code == 200
    assert response.json()["key"] == "test"


def test_read_key_value():
    response = client.get("/key_value/test")
    assert response.status_code == 200
    assert response.json()["key"] == "test"
