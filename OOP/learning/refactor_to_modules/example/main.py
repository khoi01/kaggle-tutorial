from account import BankAccount
from storage import Storage

try:
    account = BankAccount("Fayyad", 1000)
    print(account.deposit(250))
    print(account.withdraw(400))

    print("\nReloading from file...")
    loaded = Storage.load_from_file("Fayyad_account.json", BankAccount)
    print(f"Balance: ${loaded.balance}")
    print("History:", loaded.history)

except Exception as e:
    print("❌ Error:", e)
