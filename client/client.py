"""
Description: This file defines the Client class used to represent a bank client.
Author: Sukhtab Singh Warya
Date: 10/09/2024
"""

from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

class Client(Observer):
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        self._client_number = self._validate_client_number(client_number)
        self._first_name = self._validate_name(first_name, "First name")
        self._last_name = self._validate_name(last_name, "Last name")
        self._email_address = self._validate_email_address(email_address)

    @staticmethod
    def _validate_client_number(client_number: int) -> int:
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        return client_number

    @staticmethod
    def _validate_name(name: str, field_name: str) -> str:
        name = name.strip()
        if not name:
            raise ValueError(f"{field_name} cannot be blank.")
        return name

    @staticmethod
    def _validate_email_address(email_address: str) -> str:
        try:
            valid_email = validate_email(email_address)
            return valid_email.normalized
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email address: {str(e)}")

    @property
    def client_number(self) -> int:
        return self._client_number

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def email_address(self) -> str:
        return self._email_address

    def update(self, message: str) -> None:
        print(f"Notification received by {self.first_name} {self.last_name}: {message}")
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        subject = f"ALERT: Unusual Activity: {current_time}"
        email_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"

        try:
            simulate_send_email(self.email_address, subject, email_message)
        except Exception as e:
            print(f"Failed to send email to {self.email_address}: {str(e)}")

    def __str__(self) -> str:
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email_address}"
