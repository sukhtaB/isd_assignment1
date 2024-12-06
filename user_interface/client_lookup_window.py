from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot, Qt
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount


class ClientLookupWindow(LookupWindow):
    def __init__(self):
        """
        Initialize the ClientLookupWindow, load data, and set up event connections.
        """
        super().__init__()

        # Load data into dictionaries
        self.client_listing, self.accounts = load_data()

        # Connect the lookup_button click event to the on_lookup_client method
        self.lookup_button.clicked.connect(self.on_lookup_client)

        # Connect the account_table cellClicked event to the on_select_account method
        self.account_table.cellClicked.connect(self.on_select_account)

        # Connect the filter_button click event to the on_filter_clicked method
        self.filter_button.clicked.connect(self.on_filter_clicked)

        # Initialize filter widgets
        self.filter_combo_box.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_label.setText("Data is Not Currently Filtered")

    def on_lookup_client(self):
        """
        Handle the lookup button click event.
        Retrieve client details and associated accounts, and display them in the window.
        """
        # Retain the entered client number for debugging and validation
        client_number_text = self.client_number_edit.text().strip()

        # Check if the field is empty
        if not client_number_text:
            QMessageBox.warning(self, "Invalid Input", "Client Number field is empty. Please enter a Client Number.")
            return

        # Validate that the input is numeric
        if not client_number_text.isdigit():
            QMessageBox.warning(
                self, 
                "Invalid Input", 
                "Please enter a valid numeric Client Number. Example: 12345"
            )
            return

        client_number = int(client_number_text)

        # Reset display but keep the entered client number
        self.reset_display()
        self.client_number_edit.setText(client_number_text)  # Restore entered value after reset

        # Check if the client exists in the dictionary
        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Client Not Found", f"Client Number {client_number} does not exist.")
            return

        # Display client information
        client = self.client_listing[client_number]
        self.client_info_label.setText(f"{client.first_name} {client.last_name}")

        # Populate the accounts table with accounts belonging to the client
        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                # Add account details to the table
                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = QTableWidgetItem(account.date_created.strftime("%Y-%m-%d"))
                account_type_item = QTableWidgetItem(account.__class__.__name__)

                # Align items properly
                account_number_item.setTextAlignment(Qt.AlignCenter)
                balance_item.setTextAlignment(Qt.AlignRight)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                # Add items to the table
                self.account_table.setItem(row_position, 0, account_number_item)
                self.account_table.setItem(row_position, 1, balance_item)
                self.account_table.setItem(row_position, 2, date_created_item)
                self.account_table.setItem(row_position, 3, account_type_item)

        # Adjust column widths to fit content
        self.account_table.resizeColumnsToContents()

        # Enable filtering functionality
        self.toggle_filter(False)
        self.filter_button.setEnabled(True)

    @Slot(int, int)
    def on_select_account(self, row: int, column: int):
        """
        Handle the account table cell click event.
        Open the Account Details dialog for the selected account.
        """
        # Get the account number from the selected row
        account_number_item = self.account_table.item(row, 0)

        if not account_number_item:
            QMessageBox.warning(self, "Invalid Selection", "No account selected.")
            return

        try:
            account_number = int(account_number_item.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Selection", "The selected account number is not valid.")
            return

        # Validate if the account exists in the dictionary
        if account_number not in self.accounts:
            QMessageBox.warning(self, "Account Not Found", f"Account Number {account_number} does not exist.")
            return

        # Open the Account Details window
        account = self.accounts[account_number]
        account_details_window = AccountDetailsWindow(account)

        # Connect the balance_updated signal to update_data method
        account_details_window.balance_updated.connect(self.update_data)

        # Execute the dialog
        account_details_window.exec_()

    @Slot(BankAccount)
    def update_data(self, account: BankAccount):
        """
        Update the account data in the table and save it to the CSV file.
        """
        for row in range(self.account_table.rowCount()):
            if int(self.account_table.item(row, 0).text()) == account.account_number:
                # Update the balance in the table
                self.account_table.setItem(row, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                break

        # Update the accounts dictionary
        self.accounts[account.account_number] = account

        # Save the updated data to the CSV file
        update_data(account)

    def on_filter_clicked(self):
        """
        Handle the filter button click event.
        Filter or reset the account_table based on user-defined criteria.
        """
        if self.filter_button.text() == "Apply Filter":
            # Get filter criteria
            filter_column = self.filter_combo_box.currentIndex()
            filter_value = self.filter_edit.text().strip().lower()

            # Apply filter to account_table
            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, filter_column)
                if filter_value in item.text().lower():
                    self.account_table.setRowHidden(row, False)
                else:
                    self.account_table.setRowHidden(row, True)

            # Indicate that filtering is applied
            self.toggle_filter(True)
        else:
            # Reset filters
            self.toggle_filter(False)

    def toggle_filter(self, filter_on: bool):
        """
        Toggle the filter widgets and update the filter state.

        Args:
            filter_on (bool): True if filtering is applied, False otherwise.
        """
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            # Reset table visibility
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")