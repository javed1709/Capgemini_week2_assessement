'''Create an interface `IShape` with an abstract method `calculate_area()`. 
Implement it in `Rectangle` and `Circle` classes.'''
from abc import ABC,abstractmethod 
import math
class IsShape(ABC):
    @abstractmethod
    def calculate_area():
        pass
class Rectangle(IsShape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def calculate_area(self):
        print(f"area of Rectangle={self.l*self.b}")

class Circle(IsShape):
    def __init__(self,r):
        self.r=r
    def calculate_area(self):
        print(f"area of circle={math.pi*self.r*self.r}")

s=Circle(5)
t=Rectangle(6,8)
s.calculate_area()
t.calculate_area()
