class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the account balance."""
        self._account_balance += amount

    def withdraw(self, amount):
        """Subtract amount if funds are sufficient; return True if successful."""
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self._account_balance}")