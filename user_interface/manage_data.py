"""
Description: Handles reading, organizing, and updating client and bank account data from CSV files with error handling and logging.
Author: Sukhtab Singh Warya
Date: 18/11/2024
"""


import os
import sys
import csv
from datetime import datetime, date, timedelta
import logging

# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import required classes
from bank_account import ChequingAccount, SavingsAccount, InvestmentAccount, BankAccount
from client.client import Client

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE

# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))

# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')

# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')

# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')

# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')

# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************


def load_data() -> tuple[dict, dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA
    try:
        with open(clients_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    client_number = int(row["client_number"])
                    first_name = row["first_name"]
                    last_name = row["last_name"]
                    email_address = row["email_address"]

                    if not first_name or not last_name:
                        raise ValueError("First Name or Last Name cannot be blank")

                    client = Client(client_number, first_name, last_name, email_address)
                    client_listing[client_number] = client

                except Exception as e:
                    logging.error(f"Unable to create client: {e}")

    except FileNotFoundError:
        logging.error("clients.csv file not found")

    # READ ACCOUNT DATA
    try:
        with open(accounts_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    account_number = int(row["account_number"])
                    client_number = int(row["client_number"])
                    balance = float(row["balance"])
                    date_created = datetime.strptime(row["date_created"], "%Y-%m-%d").date()
                    account_type = row["account_type"]

                    # Optional fields
                    overdraft_limit = float(row["overdraft_limit"]) if row["overdraft_limit"] != "Null" else None
                    overdraft_rate = float(row["overdraft_rate"]) if row["overdraft_rate"] != "Null" else None
                    minimum_balance = float(row["minimum_balance"]) if row["minimum_balance"] != "Null" else None
                    management_fee = float(row["management_fee"]) if row["management_fee"] != "Null" else None

                    service_charge_strategy = None  # Default or mock strategy

                    if account_type == "ChequingAccount":
                        account = ChequingAccount(account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate)
                    elif account_type == "SavingsAccount":
                        account = SavingsAccount(account_number, client_number, balance, date_created, minimum_balance, service_charge_strategy)
                    elif account_type == "InvestmentAccount":
                        account = InvestmentAccount(account_number, client_number, balance, date_created, management_fee, service_charge_strategy)
                    else:
                        logging.error(f"Invalid account type for account {account_number}: {account_type}")
                        continue

                    if client_number in client_listing:
                        accounts[account_number] = account
                    else:
                        logging.error(f"Bank Account: {account_number} contains invalid Client Number: {client_number}")

                except Exception as e:
                    logging.error(f"Unable to create bank account: {e}")

    except FileNotFoundError:
        logging.error("accounts.csv file not found")

    return client_listing, accounts


def update_data(updated_account: ChequingAccount | SavingsAccount | InvestmentAccount) -> None:
    """
    Updates the accounts.csv file with the balance of the updated BankAccount.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        for row in reader:
            account_number = int(row['account_number'])
            if account_number == updated_account.account_number:
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients, accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")
