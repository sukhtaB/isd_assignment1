from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """Class representing an Investment Account that extends BankAccount."""

    BASE_SERVICE_CHARGE = 0.50
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number, client_number, balance, date_created, management_fee=2.55):
        """Initialize the Investment Account with specific attributes."""
        super().__init__(account_number, client_number, balance)

        # Validate date_created
        if not isinstance(date_created, (str, date)):
            raise ValueError("Date created must be a string or a date object.")

        self.date_created = date_created  # Store the date created

        # Validate and set management_fee
        try:
            self.management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.management_fee = 2.55

    def __str__(self):
        """Return a string representation of the Investment Account."""
        base_str = super().__str__()
        if isinstance(self.date_created, date) and self.date_created > self.TEN_YEARS_AGO:
            management_fee_str = f"${self.management_fee:.2f}"
        else:
            management_fee_str = "Waived"
        
        return (
            f"{base_str}Date Created: {self.date_created} "
            f"Management Fee: {management_fee_str} Account Type: Investment"
        )

    def get_service_charges(self):
        """Calculate the service charges for the Investment Account."""
        if isinstance(self.date_created, date) and self.date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.management_fee
