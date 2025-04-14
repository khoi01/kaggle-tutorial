import json
import os


class Storage:
    
    @staticmethod
    def save_to_file(account):
        data = {
            "owner": account.owner,
            "balance": account.balance,
            "history": account.history
        }
        with open(f"{account.owner}_account.json", "w") as f:
            json.dump(data, f, indent=2)
            
    @staticmethod
    def load_from_file(filename, BankAccountClass):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found.")
        with open(filename, "r") as f:
            data = json.load(f)
        acc = BankAccountClass(data["owner"], data["balance"])
        acc.history = data.get("history", [])
        return acc
