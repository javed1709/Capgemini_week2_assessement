'''•Create a `Product` class with attributes `name`, `price`, and `stock`.
 Write a method `check_availability(quantity)` that returns whether the 
 requested quantity is available.'''
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def check_availability(self,availability):
        if self.stock>=availability:
            print(f"Quantity of product {self.name} is availbale")
        else:
            print(f"Quantity of product {self.name} is not availale")

lst=[]

n=int(input("Enter the total products:"))
for i in range(n):
    name=input("Enter the name of product:")
    price=int(input("Enter the price of product:"))
    stock=int(input("Enter the stock product:"))
    p=Product(name,price,stock)
    lst.append(p)

for i in lst:
    q=int(input(f"Enter the desired quantity for {i.name}:"))
    i.check_availability(q)
