class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed = self.speed + amount
        print("Speed:", self.speed)

    def brake(self, amount):
        if self.speed - amount < 0:
            self.speed = 0
        else:
            self.speed = self.speed - amount

        print("Speed:", self.speed)


car = Car("BMW")
car.accelerate(50)
car.brake(20)
car.brake(50)