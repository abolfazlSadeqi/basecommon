import unittest
from app.services.password_service import hash_password, check_password, generate_password


class TestPasswordService(unittest.TestCase):

    def test_hash_password(self):
        # Arrange
        password = "mysecretpassword"
        # Act
        hashed = hash_password(password)
        # Assert
        self.assertNotEqual(hashed, password)  # Ensure the hashed password is different from the original
        self.assertTrue(check_password(password, hashed))  # Ensure the hashed password matches the original

    def test_check_password(self):
        # Arrange
        password = "mysecretpassword"
        # Act
        hashed = hash_password(password)
        # Assert
        self.assertTrue(check_password(password, hashed))  # Ensure the password check passes
        self.assertFalse(
            check_password("wrongpassword", hashed))  # Ensure the password check fails for incorrect password

    def test_generate_password(self):
        # Act
        password = generate_password()
        # Assert
        self.assertEqual(len(password), 12)  # Default length is 12
        self.assertTrue(any(char.isdigit() for char in password))  # Ensure the password contains digits
        self.assertTrue(any(char.isalpha() for char in password))  # Ensure the password contains letters
        self.assertTrue(any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in
                            password))  # Ensure the password contains special characters


if __name__ == '__main__':
    unittest.main()
