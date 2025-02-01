'''Implement a multi-level inheritance example where `Vehicle` is a base class, 
`Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.'''
class Vehicle:
    def __init__(self,make,year,model):
        self.make=make
        self.year=year
        self.model=model
    def display(self):
        print(f"Vechile Details Name:{self.make} Year:{self.year} Model:{self.model}\n")

class Car(Vehicle):
    def __init__(self,make,year,model,number_of_doors):
        super().__init__(make,year,model)
        self.number_of_doors=number_of_doors
    
    def display_car_info(self):
        print(f"Car Name:{self.make} Year:{self.year} model:{self.model} number_of_doors:{self.number_of_doors}\n")
    
class Bike(Vehicle):
    def __init__(self,make,year,model,type_of_bike):
        super().__init__(make,year,model)
        self.type_of_bike=type_of_bike
    
    def display_bike_info(self):
        print(f"Car Name:{self.make} Year:{self.year} model:{self.model} number_of_doors:{self.type_of_bike}\n")

class ElectricCar(Car):
    def __init__(self,make,year,model,number_of_doors,battery_capacity):
        super().__init__(make,year,model,number_of_doors)
        self.battery_capacity=battery_capacity
    def display_ecar_info(self):
        print(f"Car Name:{self.make} Year:{self.year} model:{self.model} number_of_doors:{self.number_of_doors}\n")
    

c=Car("Ford",2002,"Aspire",4)
b=Bike("Bajaj",2018,"Dominar","petrol")
e=ElectricCar("Audi",2020,"Q8",5,114)
c.display()
c.display_car_info()
b.display_bike_info()
e.display_ecar_info()