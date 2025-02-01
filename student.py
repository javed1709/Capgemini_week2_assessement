'''•Implement a `Student` class with a constructor that initializes 
`name` and `roll_number`. Write a method to return student details.
'''
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def show(self):
        print(f"Name: {self.name} Rollno: {self.rollno}")

st=Student("Javed",888)
st.show()
