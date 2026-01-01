class Car:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(f"Car brand is {self.brand}")


car = Car("Mercedes")
car.display_brand()
