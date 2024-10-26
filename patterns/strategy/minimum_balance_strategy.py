"""
Description: Implements the MinimumBalanceStrategy for calculating service charges based on the account's balance.
Author: Sukhtab Singh Warya
Date: 25/10/2025
"""

from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Concrete strategy for calculating service charges based on maintaining a minimum balance.
    """

    def __init__(self, minimum_balance: float, service_charge: float):
        """
        Initialize the MinimumBalanceStrategy.

        Args:
            minimum_balance (float): The minimum balance that must be maintained to avoid charges.
            service_charge (float): The service charge if the minimum balance is not maintained.
        """
        self._minimum_balance = minimum_balance
        self._service_charge = service_charge

    def calculate_service_charges(self, account_balance: float) -> float:
        """
        Calculate the service charges based on the account balance.

        Args:
            account_balance (float): The current balance of the savings account.
        
        Returns:
            float: The calculated service charges based on the balance.
        """
        if account_balance < self._minimum_balance:
            return self._service_charge
        return 0.0
