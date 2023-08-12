class BankAccount:
    """Represents a bank account."""

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposits money into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        """Returns the balance of the account."""
        return self.balance


bank_account = BankAccount("1234567890", 1000)

bank_account.deposit(100)
print(bank_account.get_balance())  # Prints 1100

bank_account.withdraw(500)
print(bank_account.get_balance())  # Prints 600