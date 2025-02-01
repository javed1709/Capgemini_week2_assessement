'''Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, 
and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.'''
from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert():
        pass
    @abstractmethod
    def update():
        pass
    @abstractmethod
    def delete():
        pass

class SQLDatabase(ABC):
    def __init__(self):
        self.lst=[]
    def insert(self,data):
        self.lst.append(data)
        print("Data successfully inserted into Relational DB")
        
    def update(self,data,newdata):
        if data in self.lst:
            self.lst[self.lst.index(data)]=newdata
            print("Data sucessfully updated in Relational DB")
        else:
            print("Data was not found in DB")
    def delete(self,data):
        if data in self.lst:
            self.lst.remove(data)
            print("Data sucessfully deleted in Relational DB")
        else:
            print("Data was not found in Relational DB")
        

class NOSQLDatabase(ABC):
    def __init__(self):
        self.lst=[]
    def insert(self,data):
        self.lst.append(data)
        print("Data successfully inserted into nQLDB")
        
    def update(self,data,newdata):
        if data in self.lst:
            self.lst[self.lst.index(data)]=newdata
            print("Data sucessfully updated in nQLDB")
        else:
            print("Data was not found in DB")
    def delete(self,data):
        if data in self.lst:
            self.lst.remove(data)
            print("Data sucessfully deleted in nQLDB")
        else:
            print("Data was not found in nQLDB")

s = SQLDatabase()

s.insert("Record1")
s.insert("Record2")
s.insert("Record3")

s.update("Record2", "UpdatedRecord2")

s.delete("Record1")
s.delete("NonExistentRecord")

print("Current SQL database state:", s.lst)

n = NOSQLDatabase()

n.insert("RecordA")
n.insert("RecordB")
n.insert("RecordC")

n.update("RecordB", "UpdatedRecordB")

n.delete("RecordA")
n.delete("NonExistentRecord")

print("Current nQL database state:", n.lst)