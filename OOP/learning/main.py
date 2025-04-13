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
    item = Product("Apple",230)
    # Access like public variable, but it's actually a method
    print(item.price)   # ✅ 2500

    # Set value with logic behind the scenes
    item.price = 3000   # ✅ Works
    print(item.price)   # 3000

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

