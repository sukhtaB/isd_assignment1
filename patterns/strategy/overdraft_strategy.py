"""
Description: The OverdraftStrategy class will inherit from the ServiceChargeStrategy abstract class.
Author: Sukhtab Singh Warya
Date: 25/10/2024
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Concrete strategy for calculating service charges for accounts with overdraft protection.
    """

    def __init__(self, overdraft_limit: float, overdraft_fee: float):
        """
        Initialize the OverdraftStrategy with an overdraft limit and an overdraft fee.
        """
        self._overdraft_limit = overdraft_limit  
        self._overdraft_fee = overdraft_fee      

    def calculate_service_charges(self, account_balance: float) -> float:
        """
        Calculate service charges based on the overdraft limit and overdraft fee.
        Charge overdraft fee if the account balance goes below zero but within the overdraft limit.
        """
        if account_balance < 0 and account_balance >= -self._overdraft_limit:
            return self._overdraft_fee
        return 0.0
