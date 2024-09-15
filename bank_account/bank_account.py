"""
Description: Defines the BankAccount class for managing bank account operations, including deposit, withdrawal, and balance updates with appropriate validations.
Author: Sukhtab Singh Warya
Date: 10/09/2024
"""


class BankAccount:
    def __init__(self, account_number, client_number, balance):
        """
        Initialize a new BankAccount instance.

        :param account_number: Integer representing the bank account number.
        :param client_number: Integer representing the client number.
        :param balance: Float representing the initial balance of the account.
        """
        # Validate and set account_number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self._account_number = account_number

        # Validate and set client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number

        # Validate and set balance
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

    @property
    def account_number(self):
        """Accessor for the account number."""
        return self._account_number

    @property
    def client_number(self):
        """Accessor for the client number."""
        return self._client_number

    @property
    def balance(self):
        """Accessor for the balance."""
        return self._balance

    def update_balance(self, amount):
        """
        Update the balance with the given amount.

        :param amount: Amount to be added to the current balance.
        """
        try:
            amount = float(amount)
            self._balance += amount
        except ValueError:
            pass  # Do not update balance if amount is invalid

    def deposit(self, amount):
        """
        Deposit the given amount into the account.

        :param amount: Amount to be deposited.
        :raises ValueError: If the deposit amount is not numeric or non-positive.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")

        self.update_balance(amount)

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account.

        :param amount: Amount to be withdrawn.
        :raises ValueError: If the withdrawal amount is not numeric, non-positive, or exceeds the balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")

        if amount > self._balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self._balance:,.2f}")

        self.update_balance(-amount)

    def __str__(self):
        """
        Returns a string representation of the bank account.
        :return: String in the format: Account Number: {account_number} Balance: ${balance}
        """
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
