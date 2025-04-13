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
        return f"{self.name} says Meow!"


def main():
    # Create objects
    dog = Dog("Buddy")
    cat = Cat("Luna")

    print(dog.speak())  # Buddy says Woof!
    print(cat.speak())  # Luna says Meow!




if __name__ == '__main__':
    main()

