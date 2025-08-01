import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models.user_model import User


class TestUserLogin:

    @pytest.fixture(autouse=True)
    def setup_user(self, session: Session):
        """Create a test user before each login test."""
        from app.security.password import hash_password

        test_user = User(
            username="testuser",
            email="test@example.com",
            password=hash_password("correctpassword"),
        )

        session.add(test_user)
        session.commit()

    def test_login_with_username_success(self, client: TestClient):
        """Test successful login with a username."""
        login_data = {
            "username": "testuser",
            "password": "correctpassword"
        }

        response = client.post("/users/login", json=login_data)
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"
        assert "id" in data

    def test_login_with_email_success(self, client: TestClient):
        """Test successful login with email."""
        login_data = {
            "email": "test@example.com",
            "password": "correctpassword"
        }

        response = client.post("/users/login", json=login_data)
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"

    def test_login_wrong_password(self, client: TestClient):
        """Test login with incorrect password."""
        login_data = {
            "username": "testuser",
            "password": "wrongpassword"
        }

        response = client.post("/users/login", json=login_data)
        assert response.status_code == 401
        assert response.json()["detail"] == "Invalid Password"

    def test_login_nonexistent_user(self, client: TestClient):
        """Test login with non-existent user."""
        login_data = {
            "username": "nonexistent",
            "password": "anypassword"
        }

        response = client.post("/users/login", json=login_data)
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"

    def test_login_no_credentials(self, client: TestClient):
        """Test login without username or email."""
        login_data = {
            "password": "somepassword"
        }

        response = client.post("/users/login", json=login_data)
        assert response.status_code == 422  # Validation error

    def test_login_empty_password(self, client: TestClient):
        """Test login with empty password."""
        login_data = {
            "username": "testuser",
            "password": ""
        }

        response = client.post("/users/login", json=login_data)
        assert response.status_code == 422