"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Sukhtab Singh Warya
Date: 10/09/2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount
from datetime import date

class TestBankAccount(unittest.TestCase):
    
    def test_init_attributes(self):
        """Test __init__ to ensure attributes are set to input values."""
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        self.assertEqual(account.account_number, 54675)
        self.assertEqual(account.client_number, 8004)
        self.assertEqual(round(account.balance, 2), 870.00)
        self.assertEqual(account.date_created, date(2024, 10, 6))

    def test_init_non_numeric_balance(self):
        """Test __init__ when non-numeric balance argument is provided."""
        account = BankAccount(54675, 8004, "non_numeric", date(2024, 10, 6))
        self.assertEqual(round(account.balance, 2), 0.00)

    def test_init_non_numeric_account_number(self):
        """Test __init__ raises ValueError for non-numeric account number."""
        with self.assertRaises(ValueError) as context:
            BankAccount("non_numeric", 8004, 870.00, date(2024, 10, 6))
        self.assertEqual(str(context.exception), "Account number must be an integer.")

    def test_init_non_numeric_client_number(self):
        """Test __init__ raises ValueError for non-numeric client number."""
        with self.assertRaises(ValueError) as context:
            BankAccount(54675, "non_numeric", 870.00, date(2024, 10, 6))
        self.assertEqual(str(context.exception), "Client number must be an integer.")

    def test_init_invalid_date_created(self):
        """Test __init__ defaults date_created to today if invalid date is given."""
        account = BankAccount(54675, 8004, 870.00, "invalid_date")
        self.assertEqual(account.date_created, date.today())

    def test_get_account_number(self):
        """Test account_number property getter.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        self.assertEqual(account.account_number, 54675)

    def test_get_client_number(self):
        """Test client_number property getter.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        self.assertEqual(account.client_number, 8004)

    def test_get_balance(self):
        """Test balance property getter.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        self.assertEqual(round(account.balance, 2), 870.00)

    def test_update_balance_positive(self):
        """Test update_balance with a positive amount.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        account.update_balance(500.00)
        self.assertEqual(round(account.balance, 2), 1370.00)

    def test_update_balance_negative(self):
        """Test update_balance with a negative amount.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        account.update_balance(-200.00)
        self.assertEqual(round(account.balance, 2), 670.00)

    def test_update_balance_non_numeric(self):
        """Test update_balance with a non-numeric amount.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        account.update_balance("non_numeric")
        self.assertEqual(round(account.balance, 2), 870.00)

    def test_deposit_valid(self):
        """Test deposit with a valid amount.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        account.deposit(250.00)
        self.assertEqual(round(account.balance, 2), 1120.00)

    def test_deposit_negative(self):
        """Test deposit with a negative amount.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        with self.assertRaises(ValueError) as context:
            account.deposit(-100.00)
        self.assertEqual(str(context.exception), "Deposit amount: $-100.00 must be positive.")

    def test_withdraw_valid(self):
        """Test withdraw with a valid amount.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        account.withdraw(300.00)
        self.assertEqual(round(account.balance, 2), 570.00)

    def test_withdraw_negative(self):
        """Test withdraw with a negative amount.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        with self.assertRaises(ValueError) as context:
            account.withdraw(-50.00)
        self.assertEqual(str(context.exception), "Withdrawal amount: $-50.00 must be positive.")

    def test_withdraw_exceeds_balance(self):
        """Test withdraw amount exceeding balance.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        with self.assertRaises(ValueError) as context:
            account.withdraw(1000.00)
        self.assertEqual(str(context.exception), "Withdrawal amount: $1000.00 must not exceed the account balance: $870.00")

    def test_str_method(self):
        """Test __str__ method.""" 
        account = BankAccount(54675, 8004, 870.00, date(2024, 10, 6))
        self.assertEqual(str(account), "Account Number: 54675 Balance: $870.00\n")

if __name__ == '__main__':
    unittest.main()
