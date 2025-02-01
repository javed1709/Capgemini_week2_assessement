'''Create a class `Employee` with properties `name`, `id`, and `department`. 
Instantiate an object and assign values dynamically.'''
class Employee:
    def __init__(self):
        name=input("Enter the name:")
        id=int(input("Enter the id:"))
        dept=input("Enter the Dept:")
        self.name=name
        self.id=id
        self.dept=dept

emp=Employee()
print(f"Name: {emp.name}, ID: {emp.id}, Dept: {emp.dept}")