class InsufficientFundsError(Exception):
    """Custom exception for when withdrawal exceeds balance."""
    pass

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("deposit must be positive.")
        self._balance = amount
        return f"{self.owner} deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self, amount):
            if amount > self._balance:
                raise InsufficientFundsError("Not enough balance to withdraw.")
            self._balance -= amount
            return f"{self.owner} withdrew ${amount}. Balance left: ${self._balance}"

class User:
    total_users = 0

    def __init__(self,username):
        self.username = username
        User.total_users+=1
    
    @classmethod
    def get_total_users(cls):
        return f"Total registered users: {User.total_users}"
    
    
    @staticmethod
    def validate_username(username):
        return username.isalnum() and len(username) >=3
        

class CreditCard:
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card ✅"

class PayPal:
    def pay(self, amount):
        return f"Paid ${amount} using PayPal 🧾"

class CryptoWallet:
    def pay(self, amount):
        return f"Paid ${amount} using Crypto Wallet ₿"

def process_payment(payment_method,amount):
        print(payment_method.pay(amount))


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with ${self.horsepower} HP started"

class Car:
    def __init__(self,brand,engine):
        self.brand = brand
        self.engine = engine
    
    def drive(self):
        return f"{self.brand} is driving.${self.engine.start()}"



class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Orice can't be negative!")
        self._price = value

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def describe(self):
        return f"{self.name} earn ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def describe(self):
        base =  super().describe() # call parent function
        return f"{base} They manage the {self.department} department."

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another child class
class Cat(Animal):
    def speak(self):
        return super().speak() 


def main():

    acc = BankAccount("Fay",500)
    try:
        print(acc.deposit(100))
        print(acc.withdraw(700))

    except InsufficientFundsError as e:
        print("❗", e)
    except ValueError as ve:
        print("⚠️", ve)


    # u1 = User('khoi')
    # u2 = User('Ahmad')

    # print(User.get_total_users())
    # print(User.validate_username("abc123"))
    # print(User.validate_username("!!"))

    # # Create instances of each payment method
    # cc = CreditCard()
    # pp = PayPal()
    # btc = CryptoWallet()

    # # Use same function with all
    # process_payment(cc, 100)
    # process_payment(pp, 50)
    # process_payment(btc, 2000)
    
    # # Create engine object
    # v6_engine = Engine(300)

    # # Inject engine into car
    # car = Car("Toyota Supra", v6_engine)

    # print(car.drive())

    # item = Product("Apple",230)
    # # Access like public variable, but it's actually a method
    # print(item.price)   # ✅ 2500

    # # Set value with logic behind the scenes
    # item.price = 3000   # ✅ Works
    # print(item.price)   # 3000

    # Try setting an invalid value
    #item.price = -500  # ❌ Raises ValueError

    # manager =Manager("khoi",20000,"IT")
    # print(manager.describe())

    # # Create objects
    # dog = Dog("Buddy")
    # cat = Cat("Luna")

    # print(dog.speak())  # Buddy says Woof!
    # print(cat.speak())  # Luna says Meow!




if __name__ == '__main__':
    main()

