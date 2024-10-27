"""
Description: This file contains the definition of the ServiceChargeStrategy class and its subclasses for calculating service charges using the Strategy Pattern.
Author: Sukhtab Singh Warya
Date: 25/10/2024
"""


from abc import ABC, abstractmethod
from datetime import date, timedelta

class ServiceChargeStrategy(ABC):
    """
    Abstract class for defining the interface for service charge calculation.
    Each account type will implement this strategy differently.
    """

    @abstractmethod
    def calculate_service_charges(self, account_balance: float) -> float:
        """
        Abstract method for calculating service charges.
        This method will be implemented in subclasses.
        
        :param account_balance: The current balance of the account.
        :return: The service charges applicable to the account.
        """
        pass


class OverdraftStrategy(ServiceChargeStrategy):
    """Concrete strategy for calculating overdraft service charges."""

    def __init__(self, overdraft_limit: float, base_service_charge: float):
        self.overdraft_limit = overdraft_limit
        self.base_service_charge = base_service_charge

    def calculate_service_charges(self, account_balance: float) -> float:
        """
        Calculate service charges based on the overdraft limit and balance.
        
        :param account_balance: The current balance of the account.
        :return: The service charge if the balance is below the overdraft limit.
        """
        if account_balance < self.overdraft_limit:
            overdraft_amount = self.overdraft_limit - account_balance
            return self.base_service_charge + (overdraft_amount * 0.05)  # Assuming 5% overdraft fee
        return self.base_service_charge


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """Concrete strategy for calculating service charges for minimum balance accounts."""

    def __init__(self, min_balance: float, service_charge: float):
        self.min_balance = min_balance
        self.service_charge = service_charge

    def calculate_service_charges(self, account_balance: float) -> float:
        """
        Calculate service charges if the balance is below the minimum required balance.
        
        :param account_balance: The current balance of the account.
        :return: The service charge if the balance is below the minimum balance.
        """
        if account_balance < self.min_balance:
            return self.service_charge
        return 0.0


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Concrete strategy for calculating management fees for investment accounts.
    """
    # Constant for the date that is 10 years ago
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