class Car:
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



def main():
    car1 = Car("Honda","Green")
    for call in range(11):
        car1.drive()


if __name__ == '__main__':
    main()
