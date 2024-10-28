"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: Sukhtab singh Warya
Date: 25/10/2024
"""

# 1. Import all BankAccount types using the bank_account package
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client  
from datetime import date  

# 2. Create a Client object with data of your choice.
client1 = Client(client_number=1, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")

# 3a. Create a ChequingAccount object for client1.
chequing_account1 = ChequingAccount(
    account_number=9876,
    client_number=client1.client_number,
    balance=50.00,
    date_created=str(date.today())
)

# 3b. Create a SavingsAccount object for client1.
savings_account1 = SavingsAccount(
    account_number=6854,
    client_number=client1.client_number,
    balance=1000.00,
    date_created=str(date.today()),
    minimum_balance=500.00,
    service_charge_strategy=None
)

# Attach client1 as an observer to both accounts.
chequing_account1.attach(client1)
savings_account1.attach(client1)

# 5a. Create a second Client object.
client2 = Client(client_number=2, first_name="Kanwarjot", last_name="Singh", email_address="kanwarjot@gmail.com")

# 5b. Create a SavingsAccount object for client2.
savings_account2 = SavingsAccount(
    account_number=5643,
    client_number=client2.client_number,
    balance=1200.00,
    date_created=str(date.today()),
    minimum_balance=500.00,
    service_charge_strategy=None
)

# Attach client2 as an observer to their own account.
savings_account1.attach(client2)

# 6. Perform three key transactions to trigger notifications.

# Transaction 1: Withdraw from chequing_account1 to trigger a low balance warning for client1
try:
    chequing_account1.withdraw(10.00)  # Should trigger low balance warning
except Exception as e:
    print(f"ChequingAccount withdraw error: {str(e)}")

# Transaction 2: Large deposit on savings_account1 for client1
try:
    savings_account1.deposit(15000.00)  # Should trigger large transaction notification for client1
except Exception as e:
    print(f"SavingsAccount1 deposit error: {str(e)}")

# Transaction 3: Withdraw from savings_account2 for client2, potentially triggering a low balance warning
try:
    savings_account2.withdraw(600.00)  # Should trigger low balance warning for client2
except Exception as e:
    print(f"SavingsAccount2 withdraw error: {str(e)}")
