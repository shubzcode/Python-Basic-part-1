class BankAccount:
    """Represents a bank account."""

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposits money into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws money from the account if sufficient balance."""
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        """Returns the current balance."""
        return self.balance

# Creating a bank account object
account = BankAccount("Ganpatrav")

print("Account holder:", account.account_holder)
print("Initial balance:", account.get_balance())

account.deposit(1000) #deposit ammount in bank account
print("Balance after deposit:", account.get_balance())

account.withdraw(200) #withdraw ammount
print("Balance after withdrawal:", account.get_balance())
