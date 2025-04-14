import json
import os
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self._balance = balance
        self.history = []

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance+=amount
        self._log("deposit",amount)
        return f"{self.owner} deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self,amount):
        if amount > self._balance:
            raise InsufficientFundsError("Not enough balance to withdraw.")
        self._balance -= amount
        self._log("withdraw",amount)
        return f"{self.owner} withdrew ${amount}. Balance left: ${self._balance}"
    
    def _log(self,action,amount):
        self.history.append({"action":action,"amount":amount})
        self.save_to_file()
    
    def save_to_file(self):
        data = {
            "owner": self.owner,
            "balance": self._balance,
            "history": self.history
        }
        with open(f"{self.owner}_account.json","w") as f:
            json.dump(data,f,indent=2)
       
    @classmethod
    def load_from_file(cls,filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found.")
        with open(filename, "r") as f:
                    data = json.load(f)
        acc = cls(data["owner"], data["balance"])
        acc.history = data.get("history", [])
        return acc

def main():
    account = BankAccount("Fayyad", 1000)
    print(account.deposit(250))
    print(account.withdraw(400))
    # To simulate reload
    print("\nReloading account from file...")
    loaded_account = BankAccount.load_from_file("Fayyad_account.json")
    print(f"Loaded {loaded_account.owner}'s balance: ${loaded_account._balance}")
    print("Transaction history:", loaded_account.history)





if __name__ == '__main__':
    main()

