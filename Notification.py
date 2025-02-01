# Implement method overriding for a `Notification` class where `send()` is overridden
#  in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        print("To communicate message multiple channels are available")
    
class EmailNotification(Notification):
    def send(self):
        super().send()
        print("communicationn through Email")

class SMSNotification(Notification):
    def send(self):
        print("communicationn through SMS")

e=EmailNotification()
s=SMSNotification()
e.send()
s.send()