"""
Description: This module defines the SavingsAccount class, which extends the BankAccount class.
Author: Sukhtab Singh Warya
Date: 06/10/2024
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import MinimumBalanceStrategy  # Ensure this import matches your structure

class SavingsAccount(BankAccount):
    """
    The SavingsAccount class represents a savings account for a banking client, allowing deposits
    and occasional withdrawals, and includes service charge calculations based on balance.
    """
    
    def __init__(self, account_number, client_number, balance, date_created, minimum_balance):
        """
        Initializes a new SavingsAccount instance.

        Parameters:
        account_number (int): The account number.
        client_number (int): The client number.
        balance (float): The initial balance.
        date_created (date): The date the account was created.
        minimum_balance (float): The minimum balance before additional service charges apply.

        If the minimum_balance cannot be converted to a float, it defaults to 50.00.
        """
        # Initialize the parent class with the required parameters
        super().__init__(account_number, client_number, balance, date_created)

        # Set the date_created attribute for SavingsAccount
        self.date_created = date_created
        
        # Validate minimum_balance and set default if necessary
        try:
            self.minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.minimum_balance = 50.00  # Default value

        # Define the MinimumBalanceStrategy instance
        self._minimum_balance_strategy = MinimumBalanceStrategy(self.minimum_balance, self.BASE_SERVICE_CHARGE)

    def __str__(self):
        """
        Returns a string representation of the SavingsAccount instance, including
        account details and minimum balance formatted as currency.

        Returns:
        str: Formatted string representation of the account.
        """
        base_str = super().__str__()  # Call the parent class's __str__ method
        return f"{base_str}Minimum Balance: ${self.minimum_balance:.2f} Account Type: Savings"

    def get_service_charges(self):
        """
        Calculates the service charges for the SavingsAccount based on the current balance
        and minimum balance using MinimumBalanceStrategy.

        Returns:
        float: The calculated service charge.
        """
        # Call the calculate_service_charges method of the MinimumBalanceStrategy instance
        return self._minimum_balance_strategy.calculate_service_charges(self.balance)
