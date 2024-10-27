"""
Description: This file defines the ChequingAccount class, which represents a chequing account with basic operations such as deposit and withdrawal.
Author: Sukhtab Singh Warya
Date: 06/10/2024
"""

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.service_charge_strategy import OverdraftStrategy  

class ChequingAccount(BankAccount):
    """Class representing a Chequing Account that extends BankAccount."""

    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit=-100, overdraft_rate=0.05):
        """Initialize the Chequing Account with specific attributes."""
        # Define the OverdraftStrategy instance first
        overdraft_strategy = OverdraftStrategy(overdraft_limit, self.BASE_SERVICE_CHARGE)
        
        # Pass the overdraft_strategy as the service_charge_strategy to the parent class
        super().__init__(account_number, client_number, balance, date_created, overdraft_strategy)

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
        """Calculate the service charges for the Chequing Account using OverdraftStrategy."""
        # Use the overdraft strategy to calculate the service charges
        return self.service_charge_strategy.calculate_service_charges(self.balance)
