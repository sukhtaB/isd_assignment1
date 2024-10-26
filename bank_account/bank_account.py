"""
Description: This file defines the BankAccount class, which represents a bank account with basic operations such as deposit and withdrawal.
Author: Sukhtab Singh Warya
Date: 10/09/2024
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class BankAccount:
    def __init__(self, account_number, client_number, balance, date_created, service_charge_strategy: ServiceChargeStrategy):
        """Initialize the bank account with account number, client number, balance, and service charge strategy.

        Args:
            account_number (int): The account number.
            client_number (int): The client number.
            balance (float or int): The initial balance of the account.
            date_created (str): The date the account was created.
            service_charge_strategy (ServiceChargeStrategy): Strategy for calculating service charges.

        Raises:
            ValueError: If account_number or client_number is not an integer, or if balance cannot be converted to float.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        
        try:
            self._balance = float(balance)
        except (ValueError, TypeError):
            self._balance = 0.0
        
        self._account_number = account_number
        self._client_number = client_number
        self.date_created = date_created
        self.service_charge_strategy = service_charge_strategy  # Set the service charge strategy

    @property
    def account_number(self):
        """Return the account number."""
        return self._account_number

    @property
    def client_number(self):
        """Return the client number."""
        return self._client_number

    @property
    def balance(self):
        """Return the balance."""
        return round(self._balance, 2)  # Round balance to 2 decimal places

    def update_balance(self, amount):
        """Update the balance with the given amount.

        Args:
            amount (float or int): The amount to be added to the balance.

        Notes:
            The amount can be negative which will decrease the balance.
        """
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            return  # If conversion fails, do nothing
        
        self._balance += amount

    def deposit(self, amount):
        """Deposit a specified amount into the account.

        Args:
            amount (float or int): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not numeric or is non-positive.
        """
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"Deposit amount must be numeric, but received: {amount}.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount):
        """Withdraw a specified amount from the account.

        Args:
            amount (float or int): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not numeric, is non-positive, or exceeds the account balance.
        """
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"Withdrawal amount must be numeric, but received: {amount}.")
        
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must be positive.")
        
        if amount > self._balance:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must not exceed the account balance: ${self._balance:.2f}")
        
        self.update_balance(-amount)

    def calculate_service_charges(self):
        """Calculate the service charges using the assigned strategy."""
        return self.service_charge_strategy.calculate_service_charges(self._balance)

    def __str__(self):
        """Return a string representation of the bank account.

        Returns:
            str: A string showing the account number and the balance.
        """
        return f"Account Number: {self._account_number} Balance: ${self._balance:.2f}\n"
