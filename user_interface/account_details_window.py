"""
Description: Manages bank account transactions (deposit, withdrawal) and displays account details using event handling and signals.
Author: Sukhtab Singh Warya
Date: 18/11/2024
"""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy


class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    # Signal to send the updated account details
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the AccountDetailsWindow.
        Args:
            account: The bank account to be displayed.
        """
        super().__init__()

        # Ensure the received account is a BankAccount instance
        if not isinstance(account, BankAccount):
            QMessageBox.critical(self, "Error", "Invalid Bank Account data provided.")
            self.reject()  # Close the dialog
            return

        # Make a copy of the account object to avoid modifying the original
        self.account = copy.deepcopy(account)

        # Populate the UI fields with account details
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(f"${self.account.balance:,.2f}")

        # Connect buttons to their respective methods
        self.deposit_button.clicked.connect(self.on_apply_transaction)
        self.withdraw_button.clicked.connect(self.on_apply_transaction)
        self.exit_button.clicked.connect(self.on_exit)

    def on_apply_transaction(self):
        """
        Handle deposit or withdrawal based on the clicked button.
        """
        try:
            # Retrieve the transaction amount
            amount_text = self.transaction_amount_edit.text().strip()

            if not amount_text:
                raise ValueError("Transaction amount is empty. Please enter an amount.")

            # Convert to a float and validate the amount
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError("Transaction amount must be greater than 0.")

            # Determine the type of transaction
            transaction_type = "Deposit" if self.sender() == self.deposit_button else "Withdraw"

            # Perform the transaction
            if transaction_type == "Deposit":
                self.account.deposit(amount)
            elif transaction_type == "Withdraw":
                self.account.withdraw(amount)

            # Update the balance label with the new balance
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Clear the transaction amount field
            self.transaction_amount_edit.clear()

            # Emit the signal with the updated account
            self.balance_updated.emit(self.account)

            # Display a success message
            QMessageBox.information(self, "Transaction Successful", f"{transaction_type} of ${amount:,.2f} completed successfully.")

        except ValueError as e:
            # Handle invalid input or transaction errors
            QMessageBox.warning(self, "Transaction Failed", str(e))
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            # Handle other exceptions (e.g., insufficient balance)
            transaction_type = "Deposit" if self.sender() == self.deposit_button else "Withdraw"
            QMessageBox.warning(self, "Transaction Failed", f"{transaction_type} failed: {str(e)}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

    def on_exit(self):
        """
        Handle the exit button to close the dialog.
        """
        self.close()
