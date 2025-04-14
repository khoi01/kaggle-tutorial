from exceptions import InsufficientFundsError
from storage import Storage

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount
        self._log("deposit", amount)
        return f"{self.owner} deposited ${amount}. New balance: ${self._balance}"

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("Not enough balance to withdraw.")
        self._balance -= amount
        self._log("withdraw", amount)
        return f"{self.owner} withdrew ${amount}. Balance left: ${self._balance}"

    def _log(self, action, amount):
        self.history.append({"action": action, "amount": amount})
        Storage.save_to_file(self)

    @property
    def balance(self):
        return self._balance
