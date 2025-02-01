'''Write a `Payment` class with a method `process_payment()`. Implement subclasses 
`CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method
 differently.'''
class Payment:
    def process_payment(self):
        print("Processing Payment by multiple methods")

class CreditCardPayment(Payment):
    def process_payment(self):
        super().process_payment()
        print("Processing Payment by CreditCardPayment")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing Payment by PayPalPayment")

class BitcoinPayment(Payment):
    def process_payment(self):
        print("Processing Payment by BitcoinPayment")

c=CreditCardPayment()
p=PayPalPayment()
b=BitcoinPayment()
c.process_payment()
p.process_payment()
b.process_payment()

