"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Sukhtab Singh Warya
Date: 10/09/2024
"""

import unittest
from client.client import Client
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase):

    def test_valid_client(self):
        """Test creating a client with valid details."""
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(client.client_number, 1010)
        self.assertEqual(client.first_name, "Sukhtab")
        self.assertEqual(client.last_name, "Warya")
        self.assertEqual(client.email_address, "sukhtabwarya@gmail.com")

    def test_invalid_client_number(self):
        """Test creating a client with an invalid client number."""
        with self.assertRaises(ValueError) as context:
            Client(client_number="not_integer", first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(str(context.exception), "Client number must be an integer.")

    def test_blank_first_name(self):
        """Test creating a client with a blank first name."""
        with self.assertRaises(ValueError) as context:
            Client(client_number=1010, first_name=" ", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(str(context.exception), "First name cannot be blank.")

    def test_blank_last_name(self):
        """Test creating a client with a blank last name."""
        with self.assertRaises(ValueError) as context:
            Client(client_number=1010, first_name="Sukhtab", last_name=" ", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(str(context.exception), "Last name cannot be blank.")

    def test_invalid_email(self):
        """Test creating a client with an invalid email address."""
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="invalid-email")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_client_number_property(self):
        """Test the client_number property."""
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(client.client_number, 1010)

    def test_first_name_property(self):
        """Test the first_name property."""
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(client.first_name, "Sukhtab")

    def test_last_name_property(self):
        """Test the last_name property."""
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(client.last_name, "Warya")

    def test_email_address_property(self):
        """Test the email_address property."""
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(client.email_address, "sukhtabwarya@gmail.com")

    def test_str_method(self):
        """Test the __str__ method."""
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        self.assertEqual(str(client), "Warya, Sukhtab [1010] - sukhtabwarya@gmail.com\n")

if __name__ == '__main__':
    unittest.main()
