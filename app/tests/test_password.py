import pytest

from app.services.pdf_service import hash_password, check_password, generate_password


def test_hash_password():
    password = "mysecretpassword"
    hashed = hash_password(password)
    assert hashed != password  # Ensure the hashed password is different from the original
    assert check_password(password, hashed)  # Ensure the hashed password matches the original

def test_check_password():
    password = "mysecretpassword"
    hashed = hash_password(password)
    assert check_password(password, hashed)  # Ensure the password check passes
    assert not check_password("wrongpassword", hashed)  # Ensure the password check fails for incorrect password

def test_generate_password():
    password = generate_password()
    assert len(password) == 12  # Default length is 12
    assert any(char.isdigit() for char in password)  # Ensure the password contains digits
    assert any(char.isalpha() for char in password)  # Ensure the password contains letters
    assert any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password)  # Ensure the password contains special characters
