class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car strated...!")
    @staticmethod
    def stop():
        print("car stopped...!")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        super().start()

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("Venue")
#
# print(car1.color)
# print(car1.name)
# print(car1.start())