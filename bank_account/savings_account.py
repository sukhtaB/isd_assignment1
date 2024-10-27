"""
Description: This module defines the SavingsAccount class, which extends the BankAccount class.
Author: Sukhtab Singh Warya
Date: 06/10/2024
"""

from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    """
    The SavingsAccount class represents a savings account for a banking client, allowing deposits
    and occasional withdrawals, and includes service charge calculations based on balance.
    """
    
    BASE_SERVICE_CHARGE = 10.00  # Define a base service charge
    SERVICE_CHARGE_PREMIUM = 2.00  # Premium multiplier for lower balances

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float, service_charge_strategy: str):
        """
        Initializes a new SavingsAccount instance.

        Parameters:
        account_number (int): The account number.
        client_number (int): The client number.
        balance (float): The initial balance.
        date_created (date): The date the account was created.
        minimum_balance (float): The minimum balance before additional service charges apply.
        service_charge_strategy (str): The strategy for calculating service charges.
        """
        # Initialize the parent class with the required parameters
        super().__init__(account_number, client_number, balance, date_created, service_charge_strategy)

        # Validate minimum_balance and set default if necessary
        try:
            self.minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.minimum_balance = 50.00  # Default value

    def __str__(self):
        """
        Returns a string representation of the SavingsAccount instance, including
        account details and minimum balance formatted as currency.

        Returns:
        str: Formatted string representation of the account.
        """
        base_str = super().__str__()  # Call the parent class's __str__ method
        return f"{base_str}Minimum Balance: ${self.minimum_balance:.2f} Account Type: Savings"

    def get_service_charges(self) -> float:
        """
        Calculates the service charges for the SavingsAccount based on the current balance
        and minimum balance.

        Returns:
        float: The calculated service charge.
        """
        if self.balance >= self.minimum_balance:
            return self.BASE_SERVICE_CHARGE  # Standard charge when above minimum balance
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM  # Higher charge when below minimum balance
