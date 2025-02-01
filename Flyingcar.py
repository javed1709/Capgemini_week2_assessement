'''Simulate multiple inheritance where `FlyingCar` inherits from both `Car`
 and `defAirplane`. Handle potential conflicts in the `move()` method.'''
class Car:
    def __init__(self,make,year,model,number_of_doors):
        self.number_of_doors=number_of_doors
    
    def display_car_info(self):
        print(f"Car Name:{self.make} Year:{self.year} model:{self.model} number_of_doors:{self.number_of_doors}\n")

class Airplane:
    def __init__(self,make,year,model,number_of_doors,wingspan):
        self.wingspan = wingspan

    def display_airplane_info(self):
        print(f"Airplane Name:{self.make} Year:{self.year} model:{self.model} wingspan:{self.wingspan}\n")

class FlyingCar(Car, Airplane):
    def __init__(self, make, year, model, number_of_doors, wingspan):
        Car.__init__(self, make, year, model, number_of_doors)
        Airplane.__init__(self, make, year, model, number_of_doors, wingspan)

    def move(self):
        print("FlyingCar can both drive and fly")

f=FlyingCar("aeromobil",2030,"skyforce",8,900)
f.move()