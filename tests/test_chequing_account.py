"""
Description: Unit tests for the ChequingAccount class.
Author: Sukhtab Singh Warya
Date: 06/10/2024
"""

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        """Set up a ChequingAccount instance for testing."""
        self.account = ChequingAccount(26355900, 8004, 850.00, date.today(), -350, 0.05)

    def test_init_attributes(self):
        """Test __init__ to ensure attributes are set correctly."""
        self.assertEqual(self.account.account_number, 26355900)
        self.assertEqual(self.account.client_number, 8004)
        self.assertEqual(round(self.account.balance, 2), 850.00)
        self.assertEqual(round(self.account.overdraft_limit, 2), -350.00)
        self.assertEqual(round(self.account.overdraft_rate, 2), 0.05)

    def test_init_invalid_overdraft_limit(self):
        """Test __init__ when overdraft limit has invalid type."""
        with self.assertRaises(ValueError):
            ChequingAccount(26355900, 8004, 850.00, date.today(), "invalid", 0.05)

    def test_init_invalid_overdraft_rate(self):
        """Test __init__ when overdraft rate has invalid type."""
        with self.assertRaises(ValueError):
            ChequingAccount(26355900, 8004, 850.00, date.today(), -350, "invalid")

    def test_init_invalid_date_created(self):
        """Test __init__ when date created has invalid type."""
        with self.assertRaises(ValueError):
            ChequingAccount(26355900, 8004, 850.00, 12345, -350, 0.05)

    def test_get_service_charges_balance_above_limit(self):
        """Test get_service_charges when balance is greater than overdraft limit."""
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_get_service_charges_balance_below_limit(self):
        """Test get_service_charges when balance is less than overdraft limit."""
        self.account.update_balance(-1200.00)  # Overdraw to -1200.00
        overdraft_amount = self.account.balance - self.account.overdraft_limit  # Calculate the overdraft
        expected_service_charge = 0.50 + (overdraft_amount * self.account.overdraft_rate)  # Calculate expected service charge
        self.assertEqual(round(self.account.get_service_charges(), 2), round(expected_service_charge, 2))

    def test_get_service_charges_balance_equal_to_limit(self):
        """Test get_service_charges when balance is equal to overdraft limit."""
        self.account.update_balance(-350.00)  # Balance is exactly at overdraft limit
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_str_method(self):
        """Test __str__ method."""
        expected_str = (
            "Account Number: 26355900 Balance: $850.00\n"
            "Overdraft Limit: $-350.00 Overdraft Rate: 5.00% Account Type: Chequing"
        )
        self.assertEqual(str(self.account), expected_str)

if __name__ == '__main__':
    unittest.main()
