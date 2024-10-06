"""
Description: This file defines the ChequingAccount class, which represents a chequing account with basic operations such as deposit and withdrawal.
Author: Sukhtab Singh Warya
Date: 06/10/2024
"""

from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """Class representing a Chequing Account that extends BankAccount."""

    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit=-100, overdraft_rate=0.05):
        """Initialize the Chequing Account with specific attributes.

        Args:
            account_number (int): The account number.
            client_number (int): The client number.
            balance (float or int): The initial balance of the account.
            date_created (date): The date the account was created.
            overdraft_limit (float): The maximum amount the balance can be overdrawn.
            overdraft_rate (float): The rate for overdraft fees.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Validate and set overdraft_limit
        try:
            self._overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self._overdraft_limit = -100.0

        # Validate and set overdraft_rate
        try:
            self._overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self._overdraft_rate = 0.05

    @property
    def overdraft_limit(self):
        """Return the overdraft limit."""
        return self._overdraft_limit

    @property
    def overdraft_rate(self):
        """Return the overdraft rate."""
        return self._overdraft_rate

    def __str__(self):
        """Return a string representation of the Chequing Account.

        Returns:
            str: A string showing account details.
        """
        base_str = super().__str__()
        return (
            f"{base_str}Overdraft Limit: ${self._overdraft_limit:.2f} "
            f"Overdraft Rate: {self._overdraft_rate * 100:.2f}% Account Type: Chequing"
        )

    def get_service_charges(self):
        """Calculate the service charges for the Chequing Account.

        Returns:
            float: The calculated service charges.
        """
        if self.balance >= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return (
                self.BASE_SERVICE_CHARGE +
                (self._overdraft_limit - self.balance) * self._overdraft_rate
            )
