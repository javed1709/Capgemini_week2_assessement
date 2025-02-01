'''Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` 
classes that provide specific implementations for `area()`.'''
class Shape:
    def area(self):
        print("Every shape hae Unique Area")

class Square(Shape):
    def __init__(self,sl):
        self.sl=sl
    def area(self):
        super().area()
        print(f"area of Square={self.sl*self.sl}")

class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        print(f"area of Triangle={0.5*self.b*self.h}")

s=Square(5)
t=Triangle(6,8)
s.area()
t.area()
