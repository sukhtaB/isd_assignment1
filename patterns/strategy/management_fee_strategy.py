"""
Description: Implements the ManagementFeeStrategy class for calculating service charges for investment accounts.
Author: Sukhtab Singh Warya
Date: 25/10/2024
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Concrete strategy for calculating management fees for investment accounts.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, annual_fee: float, account_creation_date: date):
        """
        Initialize the ManagementFeeStrategy with the annual fee and account creation date.
        """
        self._annual_fee = annual_fee  # Protected attribute
        self._account_creation_date = account_creation_date  # Protected attribute

    def calculate_service_charges(self, account_balance: float) -> float:
        """
        Calculate service charges based on the annual management fee.
        If the account is older than 10 years, apply half of the fee.
        """
        if self._account_creation_date < ManagementFeeStrategy.TEN_YEARS_AGO:
            return self._annual_fee / 2
        return self._annual_fee
