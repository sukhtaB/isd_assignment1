"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: Sukhtab Singh Warya
Date: 06/10/2024
"""

# 1. Import all BankAccount types using the bank_account package
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your choice 
# including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(26355900, 8004, 200.00, date.today(), -350.00, 0.05)
except Exception as e:
    print(f"Error creating ChequingAccount: {e}")

# 3. Print the ChequingAccount created in step 2.
print("Chequing Account:")
print(chequing_account)

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print("Service Charges:", chequing_account.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
try:
    chequing_account.update_balance(200.00)  # Deposit to avoid overdraft
except Exception as e:
    print(f"Error updating balance: {e}")

# 4b. Print the ChequingAccount
print("\nAfter Deposit:")
print(chequing_account)

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print("Service Charges:", chequing_account.get_service_charges())

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(26350095, 4008, 150.00, date.today(), 50.00)
except Exception as e:
    print(f"Error creating SavingsAccount: {e}")

# 6. Print the SavingsAccount created in step 5.
print("Savings Account:")
print(savings_account)

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print("Service Charges:", savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
try:
    savings_account.update_balance(-101.00)  # Withdraw to drop below minimum
except Exception as e:
    print(f"Error updating balance: {e}")

# 7b. Print the SavingsAccount.
print("\nAfter Withdrawal:")
print(savings_account)

# 7c. Print the service charges amount if calculated based on the current state of the SavingsAccount created in step 5.
print("Service Charges:", savings_account.get_service_charges())

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account_recent = InvestmentAccount(59002635, 5550, 2000.00, date.today(), 2.00)
except Exception as e:
    print(f"Error creating InvestmentAccount: {e}")

# 9a. Print the InvestmentAccount created in step 8.
print("Recent Investment Account:")
print(investment_account_recent)

# 9b. Print the service charges amount if calculated based on the current state of the InvestmentAccount created in step 8.
print("Service Charges:", investment_account_recent.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your choice 
# including a date created prior to 10 years ago.
try:
    investment_account_old = InvestmentAccount(59002636, 5551, 2500.00, date.today() - timedelta(days=11*365), 2.00)
except Exception as e:
    print(f"Error creating old InvestmentAccount: {e}")

# 11a. Print the InvestmentAccount created in step 10.
print("\nOld Investment Account:")
print(investment_account_old)

# 11b. Print the service charges amount if calculated based on the current state of the InvestmentAccount created in step 10.
print("Service Charges:", investment_account_old.get_service_charges())

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8, and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing_account.update_balance(-chequing_account.get_service_charges())
    savings_account.update_balance(-savings_account.get_service_charges())
    investment_account_recent.update_balance(-investment_account_recent.get_service_charges())
    investment_account_old.update_balance(-investment_account_old.get_service_charges())
except Exception as e:
    print(f"Error updating balances: {e}")

# 13. Print each of the bank account objects created in steps 2, 5, 8, and 10.
print("\nFinal Account States:")
print(chequing_account)
print(savings_account)
print(investment_account_recent)
print(investment_account_old)
