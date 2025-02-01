'''Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, 
`multiply()`, and `divide()`. Create a `BasicCalculator` class that implements 
these methods.'''
from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add():
        pass
    @abstractmethod
    def subtract():
        pass
    @abstractmethod
    def multiply():
        pass
    @abstractmethod
    def divide():
        pass

class BasicCalculator(ICalculator):
    def add(self,a,b):
        print(f"a+b={a+b}")
    def subtract(self,a,b):
        print(f"a-b={a-b}")
    def multiply(self,a,b):
        print(f"a*b={a*b}")
    def divide(self,a,b):
        print(f"a/b={a/b}")
    
bc=BasicCalculator()
bc.add(10,12)
bc.subtract(34,9)
bc.multiply(12,45)
bc.divide(12,9)
