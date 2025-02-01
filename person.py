''' Create a multi-level class structure with `Person` → `Employee` → `Manager`, 
where `Manager` has an additional method `approve_leave()`.'''
class Person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name:{self.name}\nSalary:{self.salary}\n")
class Employee(Person):
    def __init__(self,name,employeeid,salary):
        super().__init__(name,salary)
        self.employeeid=employeeid

    def display_employe(self):
        print(f"id:{self.employeeid}\n")

class Manager(Employee):
    def __init__(self,name,managerid,salary):
        super().__init__(name,managerid,salary)
        self.managerid=managerid
    def approve_leave(self):
        print(f"Leave approved by Manager {self.name}")


m=Manager("John",24,30000)
m.display()
m.display_employe()
m.approve_leave()