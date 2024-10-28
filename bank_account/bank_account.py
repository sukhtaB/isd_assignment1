"""
Description: This file defines the BankAccount class, which represents a bank account with basic operations such as deposit and withdrawal.
Author: Sukhtab Singh Warya
Date: 10/09/2024
"""

from abc import ABC
from patterns.observer.subject import Subject
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class BankAccount(Subject, ABC):
    LOW_BALANCE_LEVEL = 50.00
    LARGE_TRANSACTION_THRESHOLD = 10000.00

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: str, service_charge_strategy: ServiceChargeStrategy):
        super().__init__()
        if not isinstance(account_number, int) or not isinstance(client_number, int):
            raise ValueError("Account and client numbers must be integers.")
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance if isinstance(balance, float) else 0.0
        self.date_created = date_created
        self.service_charge_strategy = service_charge_strategy

    @property
    def account_number(self):
        return self._account_number

    @property
    def client_number(self):
        return self._client_number

    @property
    def balance(self):
        return round(self._balance, 2)

    def update_balance(self, amount: float):
        self._balance += amount
        if self._balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning: ${self.balance:.2f} on account {self._account_number}.")
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction: ${amount:.2f} on account {self._account_number}.")

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must be positive.")
        if amount > self._balance:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must not exceed the account balance: ${self.balance:.2f}")
        self.update_balance(-amount)

    def calculate_service_charges(self):
        return self.service_charge_strategy.calculate_service_charges(self._balance) if self.service_charge_strategy else 0.0

    def __str__(self):
        """Return a string representation of the Bank Account."""
        return f"Account Number: {self._account_number} Balance: ${self.balance:.2f}\n"
