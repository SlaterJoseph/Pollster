import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.security.password import hash_password, verify_password


class TestPasswordSecurity:

    def test_password_hash_verify(self):
        """Test password hashing and verification."""

        plain_password = "mysecretpassword"
        hashed = hash_password(plain_password)

        assert hashed != plain_password  # Should be hashed
        assert verify_password(plain_password, hashed) is True
        assert verify_password("wrongpassword", hashed) is False

    def test_password_hash_unique(self):
        """Test that the same password generates different hashes."""
        from app.security.password import hash_password

        password = "testpassword123"
        hash1 = hash_password(password)
        hash2 = hash_password(password)

        # Bcrypt should generate different hashes for same password
        assert hash1 != hash2