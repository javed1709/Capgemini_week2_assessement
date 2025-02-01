'''Design a system where a base class `Animal` has a method `speak()`,
 and subclasses `Dog` and `Cat` override it.'''
class Animal:
    def speak():
        pass
class Dog(Animal):
    def __init__(self,sound):
        self.sound=sound
    def speak(self):
        print(f"Dog sounds as {self.sound}")

class Cat(Animal):
    def __init__(self,sound):
        self.sound=sound
    def speak(self):
        print(f"Cat sounds as {self.sound}")

d=Dog("bow")
c=Cat("meow")
d.speak()
c.speak()