'''Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits
 from `Electronics`. Demonstrate method overriding and attribute reuse.'''
class Electronics:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print(f"Brand is {self.brand} of model {self.model} and price {self.price}")

class MobileDevice(Electronics):
    def __init__(self,brand,model,price,battery_life):
        super().__init__(brand,model,price)
        self.batter_life=battery_life
    def display(self):
        super().display()
        print(f"batter life:{self.batter_life}")

class SmartPhone(MobileDevice):
    def __init__(self,brand,model,price,battery_life,camera_quality):
        super().__init__(brand,model,price,battery_life)
        self.camera_quality=camera_quality
    def display(self):
        super().display()
        print(f"Camer quality is :{self.camera_quality}")

s=SmartPhone("smasung","S25",98000,2,160)
s.display()
    
