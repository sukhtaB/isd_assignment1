"""
Description: This file defines the ChequingAccount class, which represents a chequing account with basic operations such as deposit and withdrawal.
Author: Sukhtab Singh Warya
Date: 06/10/2024
"""

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """Class representing a Chequing Account that extends BankAccount."""

    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit=-100, overdraft_rate=0.05):
        """Initialize the Chequing Account with specific attributes."""
        super().__init__(account_number, client_number, balance)

        # Validate date_created
        if not isinstance(date_created, (str, date)):
            raise ValueError("Date created must be a string or a date object.")
        
        self.date_created = date_created  # Store the date created

        # Validate and set overdraft_limit
        if not isinstance(overdraft_limit, (int, float)):
            raise ValueError("Overdraft limit must be numeric.")
        self._overdraft_limit = float(overdraft_limit)

        # Validate and set overdraft_rate
        if not isinstance(overdraft_rate, (int, float)):
            raise ValueError("Overdraft rate must be numeric.")
        self._overdraft_rate = float(overdraft_rate)

    @property
    def overdraft_limit(self):
        """Return the overdraft limit."""
        return self._overdraft_limit

    @property
    def overdraft_rate(self):
        """Return the overdraft rate."""
        return self._overdraft_rate

    def __str__(self):
        """Return a string representation of the Chequing Account."""
        base_str = super().__str__()
        return (
            f"{base_str}Overdraft Limit: ${self._overdraft_limit:.2f} "
            f"Overdraft Rate: {self._overdraft_rate * 100:.2f}% Account Type: Chequing"
        )

    def get_service_charges(self):
        """Calculate the service charges for the Chequing Account."""
        if self.balance >= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            # Calculate how much the balance is overdrawn
            overdrawn_amount = self._overdraft_limit - self.balance  # Should be a positive amount
            return self.BASE_SERVICE_CHARGE + (overdrawn_amount * self._overdraft_rate)
