import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.models.user_model import User

class TestUserRegistration:

    def test_register_user_sucess(self, client: TestClient):
        """Test standard registration"""
        user_data = {
            'username': 'peter pan',
            'email': 'ppan@gmail.com',
            'confirm_email': 'ppan@gmail.com',
            'password': 'tinkerbell111',
            'confirm_password': 'tinkerbell111'
        }

        response = client.post('/users/register', json=user_data)

        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "peter pan"
        assert data["email"] == "ppan@gmail.com"
        assert "id" in data
        assert "password" not in data

    def test_register_user_password_mismatch(self, client: TestClient):
        """Test registration with mismatched passwords."""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "confirm_email": "test@example.com",
            "password": "password123",
            "confirm_password": "password456"
        }

        response = client.post("/users/register", json=user_data)

        assert response.status_code == 422

    def test_register_user_email_mismatch(self, client: TestClient):
        """Test registration with mismatched emails."""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "confirm_email": "different@example.com",
            "password": "password123",
            "confirm_password": "password123"
        }

        response = client.post("/users/register", json=user_data)

        assert response.status_code == 422

    def test_register_user_missing_fields(self, client: TestClient):
        """Test registration with missing required fields."""
        user_data = {
            "username": "testuser",
            "email": "test@example.com"
        }

        response = client.post("/users/register", json=user_data)

        assert response.status_code == 400

    def test_register_duplicate_username(self, client: TestClient, session: Session):
        """Test registration with duplicate username."""
        existing_user = User(
            username="existinguser",
            email="existing@example.com",
            password="hashedpassword",
            photo="",
            description=""
        )
        session.add(existing_user)
        session.commit()

        user_data = {
            "username": "existinguser",
            "email": "new@example.com",
            "confirm_email": "new@example.com",
            "password": "password123",
            "confirm_password": "password123"
        }

        response = client.post("/users/register", json=user_data)
        assert response.status_code == 400