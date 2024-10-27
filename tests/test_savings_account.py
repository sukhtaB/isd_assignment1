"""
Description: Unit tests for the SavingsAccount class.
Author: SUkhtab Singh Warya
Date: 06/10/2024
"""


import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        """Set up a basic SavingsAccount instance for testing."""
        self.account_valid = SavingsAccount(26350095, 4008, 1400.00, date.today(), 50.00, "standard")

    def test_init_attributes(self):
        """Test __init__ to ensure attributes are set to parameter values."""
        self.assertEqual(self.account_valid.account_number, 26350095)
        self.assertEqual(self.account_valid.client_number, 4008)
        self.assertEqual(round(self.account_valid.balance, 2), 1400.00)
        self.assertEqual(self.account_valid.date_created, date.today())
        self.assertEqual(round(self.account_valid.minimum_balance, 2), 50.00)

    def test_init_invalid_minimum_balance_type(self):
        """Test __init__ when minimum_balance has an invalid type."""
        account_invalid_balance = SavingsAccount(26350095, 4008, 1400.00, date.today(), "invalid", "standard")
        self.assertEqual(round(account_invalid_balance.minimum_balance, 2), 50.00)

    def test_get_service_charges_balance_greater_than_minimum_balance(self):
        """Test get_service_charges when balance is greater than minimum balance."""
        expected_charge = SavingsAccount.BASE_SERVICE_CHARGE
        self.assertEqual(round(self.account_valid.get_service_charges(), 2), round(expected_charge, 2))

    def test_get_service_charges_balance_equal_to_minimum_balance(self):
        """Test get_service_charges when balance is equal to minimum balance."""
        account_equal_balance = SavingsAccount(26350095, 4008, 50.00, date.today(), 50.00, "standard")
        expected_charge = SavingsAccount.BASE_SERVICE_CHARGE
        self.assertEqual(round(account_equal_balance.get_service_charges(), 2), round(expected_charge, 2))

    def test_get_service_charges_balance_less_than_minimum_balance(self):
        """Test get_service_charges when balance is less than minimum balance."""
        account_low_balance = SavingsAccount(26350095, 4008, 49.99, date.today(), 50.00, "standard")
        expected_charge = SavingsAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM
        self.assertEqual(round(account_low_balance.get_service_charges(), 2), round(expected_charge, 2))

    def test_str_appropriate_value_returned(self):
        """Test __str__ returns appropriate value based on attribute values."""
        expected_str = ("Account Number: 26350095 Balance: $1400.00\n"
                        "Minimum Balance: $50.00 Account Type: Savings")
        self.assertEqual(str(self.account_valid), expected_str)

if __name__ == '__main__':
    unittest.main()
