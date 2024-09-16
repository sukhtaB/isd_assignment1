"""
Description: This file defines the Client class used to represent a bank client.
Author: Sukhtab Singh Warya
Date: 10/09/2024
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initialize a new Client instance.

        :param client_number: Integer representing the client's number.
        :param first_name: String representing the client's first name.
        :param last_name: String representing the client's last name.
        :param email_address: String representing the client's email address.
        """
        # Validate and set client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number

        # Validate and set first_name
        first_name = first_name.strip()
        if not first_name:
            raise ValueError("First name cannot be blank.")
        self._first_name = first_name

        # Validate and set last_name
        last_name = last_name.strip()
        if not last_name:
            raise ValueError("Last name cannot be blank.")
        self._last_name = last_name

        # Validate email address using email-validator
        try:
            valid_email = validate_email(email_address)
            self._email_address = valid_email.normalized
        except EmailNotValidError:
            self._email_address = "email@pixell-river.com"

    @property
    def client_number(self):
        """
        Accessor for the client number.
        :return: The client's number as an integer.
        """
        return self._client_number

    @property
    def first_name(self):
        """
        Accessor for the client's first name.
        :return: The client's first name as a string.
        """
        return self._first_name

    @property
    def last_name(self):
        """
        Accessor for the client's last name.
        :return: The client's last name as a string.
        """
        return self._last_name

    @property
    def email_address(self):
        """
        Accessor for the client's email address.
        :return: The client's email address as a string.
        """
        return self._email_address

    def __str__(self):
        """
        Returns a string representation of the client.
        :return: String in the format: {last_name}, {first_name} [{client_number}] - {email_address}
        """
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email_address}\n"
