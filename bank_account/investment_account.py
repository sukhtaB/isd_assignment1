"""
Description: This file defines the InvestmentAccount class, which represents a investment account with basic operations such as deposit and withdrawal.
Author: Sukhtab Singh Warya
Date: 06/10/2024

"""
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    BASE_SERVICE_CHARGE = 10.00

    def __init__(self, account_number, client_number, balance, date_created, management_fee, service_charge_strategy):
        """
        Initialize an InvestmentAccount instance with account details.
        Also, initialize the management fee strategy.
        """
        if not isinstance(management_fee, (int, float)):
            raise TypeError("Management fee must be a number")
        
        super().__init__(account_number, client_number, balance, date_created, service_charge_strategy)
        self.management_fee = management_fee
        self._management_fee_strategy = ManagementFeeStrategy(annual_fee=self.management_fee, account_creation_date=self.date_created)

    def get_service_charges(self) -> float:
        """
        Calculate the service charges using the ManagementFeeStrategy.
        If the account is more than 10 years old, return only the base service charge.
        """
        if self.date_created <= date.today() - timedelta(days=10 * 365.25):
            return InvestmentAccount.BASE_SERVICE_CHARGE
        return InvestmentAccount.BASE_SERVICE_CHARGE + self.management_fee

    def __str__(self) -> str:
        """
        Return the string representation of the InvestmentAccount.
        If the account is more than 10 years old, waive the management fee.
        """
        if self.date_created <= date.today() - timedelta(days=10 * 365.25):
            fee_str = "Waived"
        else:
            fee_str = f"${self.management_fee:.2f}"
        return (f"Account Number: {self.account_number} Balance: ${self.balance:.2f}\n"
                f"Date Created: {self.date_created} Management Fee: {fee_str} Account Type: Investment")
