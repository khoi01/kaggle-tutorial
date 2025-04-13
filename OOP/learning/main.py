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
    manager =Manager("khoi",20000,"IT")
    print(manager.describe())

    # # Create objects
    # dog = Dog("Buddy")
    # cat = Cat("Luna")

    # print(dog.speak())  # Buddy says Woof!
    # print(cat.speak())  # Luna says Meow!




if __name__ == '__main__':
    main()

