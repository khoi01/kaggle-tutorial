
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        return f"{self.owner} deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            return f"{self.owner} withdrew ${amount}. Balance: ${self.balance}"
        else:
            return f"insufficient fund!"
           
    
class Car:
    wheels = 4 #Class Variable (shared)
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        self.fuel = 100 #full tank

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 10
            print(f"{self.brand} is driving.Fuel left: {self.fuel}")
        else:
            print(f"{self.brand} can't drive. Out of fuel!")
    
    def refuel(self):
        self.fuel = 100
        print(f"{self.brand} refueled to full tank.")
    
    def info(self):
            return f"{self.color} {self.brand} with {Car.wheels} wheels"


class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name}: woof!!"

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def get_info(self):
        return f"{self.name} score {self.grade}"

    def is_passing(self):
        return self.grade >= 60
            
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def summary(self):
        return f"{self.title} by {self.author}, costs ${self.price}"



def main():

    car1 = Car("toyota","red")
    car2 = Car("honda","dark blue")
    car3 = Car("Proton","Yellow")
    car3.wheels = 6
    print(car1.info())
    print(car2.info())
    print(car3.info())
    print(car3.wheels)
    print(Car.wheels)

    # acc = BankAccount("Ali",1000)
    # print(acc.deposit(500))
    # print(acc.withdraw(1000))
    # Creating objects (constructor is called)
    # b1 = Book("Atomic Habits", "James Clear", 89)
    # b2 = Book("Clean Code", "Robert C. Martin", 120)

    #print(b1.summary())  # Atomic Habits by James Clear, costs $89
    #print(b2.summary())  # Clean Code by Robert C. Martin, costs $120

    # s1 = Student("ahmad",70)
    # s2 = Student("razak",50)

    # print(s1.get_info())
    # print("passing?",s1.is_passing())
    # print(s2.get_info())
    # print("passing?",s2.is_passing())


    # dog1 = Dog("puppy","Standard Dog")
    # print(dog1.bark())

    # car1 = Car("Honda","Green")
    # for call in range(11):
    #     car1.drive()


if __name__ == '__main__':
    main()
