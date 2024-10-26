"""
Description: This file contains the definition of the ServiceChargeStrategy class and its subclasses for calculating service charges using the Strategy Pattern.
Author: Sukhtab Singh Warya
Date: 25/10/2024
"""

from abc import ABC, abstractmethod

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

