"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    
    def test_init_attributes(self):
        """Test __init__ to ensure attributes are set to input values."""
        account = BankAccount(12345, 67890, 1000.0)
        self.assertEqual(account.account_number, 12345)
        self.assertEqual(account.client_number, 67890)
        self.assertEqual(round(account.balance, 2), 1000.0)

    def test_init_non_numeric_balance(self):
        """Test __init__ when non-numeric balance argument is provided."""
        account = BankAccount(12345, 67890, "non_numeric")
        self.assertEqual(round(account.balance, 2), 0.0)

    def test_init_non_numeric_account_number(self):
        """Test __init__ raises ValueError for non-numeric account number."""
        with self.assertRaises(ValueError) as context:
            BankAccount("non_numeric", 67890, 1000.0)
        self.assertEqual(str(context.exception), "Account number must be an integer.")

    def test_init_non_numeric_client_number(self):
        """Test __init__ raises ValueError for non-numeric client number."""
        with self.assertRaises(ValueError) as context:
            BankAccount(12345, "non_numeric", 1000.0)
        self.assertEqual(str(context.exception), "Client number must be an integer.")

    def test_get_account_number(self):
        """Test account_number property getter."""
        account = BankAccount(12345, 67890, 1000.0)
        self.assertEqual(account.account_number, 12345)

    def test_get_client_number(self):
        """Test client_number property getter."""
        account = BankAccount(12345, 67890, 1000.0)
        self.assertEqual(account.client_number, 67890)

    def test_get_balance(self):
        """Test balance property getter."""
        account = BankAccount(12345, 67890, 1000.0)
        self.assertEqual(round(account.balance, 2), 1000.0)

    def test_update_balance_positive(self):
        """Test update_balance with a positive amount."""
        account = BankAccount(12345, 67890, 1000.0)
        account.update_balance(500.0)
        self.assertEqual(round(account.balance, 2), 1500.0)

    def test_update_balance_negative(self):
        """Test update_balance with a negative amount."""
        account = BankAccount(12345, 67890, 1000.0)
        account.update_balance(-200.0)
        self.assertEqual(round(account.balance, 2), 800.0)

    def test_update_balance_non_numeric(self):
        """Test update_balance with a non-numeric amount."""
        account = BankAccount(12345, 67890, 1000.0)
        account.update_balance("non_numeric")
        self.assertEqual(round(account.balance, 2), 1000.0)

    def test_deposit_valid(self):
        """Test deposit with a valid amount."""
        account = BankAccount(12345, 67890, 1000.0)
        account.deposit(250.0)
        self.assertEqual(round(account.balance, 2), 1250.0)

    def test_deposit_negative(self):
        """Test deposit with a negative amount."""
        account = BankAccount(12345, 67890, 1000.0)
        with self.assertRaises(ValueError) as context:
            account.deposit(-100.0)
        self.assertEqual(str(context.exception), "Deposit amount: $-100.0 must be positive.")

    def test_withdraw_valid(self):
        """Test withdraw with a valid amount."""
        account = BankAccount(12345, 67890, 1000.0)
        account.withdraw(300.0)
        self.assertEqual(round(account.balance, 2), 700.0)

    def test_withdraw_negative(self):
        """Test withdraw with a negative amount."""
        account = BankAccount(12345, 67890, 1000.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(-50.0)
        self.assertEqual(str(context.exception), "Withdrawal amount: $-50.0 must be positive.")

    def test_withdraw_exceeds_balance(self):
        """Test withdraw amount exceeding balance."""
        account = BankAccount(12345, 67890, 1000.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(1500.0)
        self.assertEqual(str(context.exception), "Withdrawal amount: $1500.0 must not exceed the account balance: $1000.0")

    def test_str_method(self):
        """Test __str__ method."""
        account = BankAccount(12345, 67890, 1000.0)
        self.assertEqual(str(account), "Account Number: 12345 Balance: $1000.00\n")

if __name__ == '__main__':
    unittest.main()
