'''Design a `BankAccount` class with `deposit()` and `withdraw()` methods.
 Implement logic to prevent overdraft.'''
class BankAccount:
    def __init__(self):
        self.money=0
    def deposit(self,amnt):
        self.money +=amnt
    def withdraw(self,amnt):
        if self.money>=amnt:
            self.money -=amnt
        else:
            print("Insufficient Funds...")
    
bn=BankAccount()
bn.deposit(200)
print(bn.money)
bn.withdraw(100)
print(bn.money)
