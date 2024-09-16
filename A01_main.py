""""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: Sukhtab Singh Warya
Date: 10/09/2024S
"""
from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """
    from client.client import Client  # Import the Client class
    from bank_account.bank_account import BankAccount  # Import the BankAccount class

    # 1. Code a statement which creates a valid instance of the Client class.
    try:
        client = Client(client_number=1010, first_name="Sukhtab", last_name="Warya", email_address="sukhtabwarya@gmail.com")
        print(f"Client created successfully: {client}")
    except Exception as e:
        print(f"Error creating Client: {e}")

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    try:
        bank_account = BankAccount(account_number=54675, client_number=client.client_number, balance=500.00)
        print(f"BankAccount created successfully: {bank_account}")
    except Exception as e:
        print(f"Error creating BankAccount: {e}")

    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use an INVALID value (non-float) for the balance.
    try:
        invalid_account = BankAccount(account_number=54321, client_number=client.client_number, balance="invalid_balance")
        print(f"BankAccount with invalid balance created successfully: {invalid_account}")
    except Exception as e:
        print(f"Error creating BankAccount with invalid balance: {e}")

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print(f"Client instance: {client}")
    print(f"BankAccount instance: {bank_account}")

    # 6. Attempt to deposit a non-numeric value into the BankAccount created in step 3.
    try:
        bank_account.deposit("non_numeric")
    except Exception as e:
        print(f"Error depositing non-numeric value: {e}")

    # 7. Attempt to deposit a negative value into the BankAccount created in step 3.
    try:
        bank_account.deposit(-100.00)
    except Exception as e:
        print(f"Error depositing negative value: {e}")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount created in step 3.
    try:
        bank_account.withdraw(150.00)
        print(f"Withdrawal successful. Updated BankAccount: {bank_account}")
    except Exception as e:
        print(f"Error withdrawing valid amount: {e}")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount created in step 3.
    try:
        bank_account.withdraw("non_numeric")
    except Exception as e:
        print(f"Error withdrawing non-numeric value: {e}")

    # 10. Attempt to withdraw a negative value from the BankAccount created in step 3.
    try:
        bank_account.withdraw(-50.00)
    except Exception as e:
        print(f"Error withdrawing negative value: {e}")

    # 11. Attempt to withdraw a value from the BankAccount created in step 3 which 
    # exceeds the current balance of the account.
    try:
        bank_account.withdraw(1000.00)
    except Exception as e:
        print(f"Error withdrawing amount exceeding balance: {e}")

    # 12. Code a statement which prints the BankAccount instance created in step 3.
    print(f"Final BankAccount instance: {bank_account}")

if __name__ == "__main__":
    main()
