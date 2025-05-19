class Car:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is started")

car = Car("Honda")
print(car.brand)
car.start()
