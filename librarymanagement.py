'''You are building a Library Management System.Create a `Book` class with properties
 like `title`, `author`, and `isbn`. Write a method to display book details.
'''
class Book:
    library={}
    def __init__(self):
        self.library={}

    def add_book(self,isb,book_details):
        if self.library.get(isb,False)==False:
            self.library[isb]=book_details
        else:
            self.library[isb][2] +=1
    
    def find_book(self,isbn):
        return self.library[isbn]
    
    def remove_book(self,isbn):
        if self.library[isbn][2]>0:
            self.library[isbn][2] -=1
        else:
            del self.library[isbn]
    def display_library(self):
        # for i in self.library:
        #     lst=list(self.library[i])
        #     print(f"isbn:{i}, Title:{lst[0]} , Author: {lst[1]}, no of copies lst[2]")
        print(self.library)


b1,b2,b3=Book(),Book(),Book()
b1.add_book("1234567891012",["Trignometry","G.tiwani",12])
b2.add_book("2234567891012",["Trignometry","G.riwani",14])
b3.add_book("3234567891012",["Trignometry","G.siwani",18])
b1.display_library()
b1.remove_book("1234567891012")
b1.display_library()
b2.display_library()
b2.remove_book("2234567891012")
b3.display_library()
b3.remove_book("3234567891012")