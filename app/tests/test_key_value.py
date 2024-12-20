import unittest
from fastapi.testclient import TestClient
from app.api.endpoints.key_value import get_db
from app.main import app
from app.db.session import SessionLocal

client = TestClient(app)


def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


class TestKeyValueAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # این متد یک بار قبل از اجرای تمام تستها اجرا میشود
        pass

    @classmethod
    def tearDownClass(cls):
        # این متد یک بار بعد از اجرای تمام تستها اجرا میشود
        pass

    def setUp(self):
        # این متد قبل از هر تست اجرا میشود
        pass

    def tearDown(self):
        # این متد بعد از هر تست اجرا میشود
        pass

    def test_create_key_value(self):
        # Arrange
        key = "test"
        value = "test_value"
        title = "test_title"
        # Act
        response = client.post("/key_value/", json={"key": key, "value": value, "title": title})
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["key"], "test")

    def test_read_key_value(self):
        # Arrange
        url = "/key_value/test"
        # Act
        response = client.get(url)
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["key"], "test")


if __name__ == '__main__':
    unittest.main()
