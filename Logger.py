'''Create a class `Logger` with a method `log(message)`. Implement 
method overloading to log different message types (`error`, `warning`, `info`).'''
class Loger:
    def log(self,message=None,message_type="unknown"): #overloading based on default 
        if message_type=="error":
            print(f"[ERROR] {message}")
        elif message_type=="warning":
            print(f"[WARNING]:{message}")
        elif message_type=="info":
            print(f"[INFO]:{message}")
        else:
            print(f"[UNKNOWN]:{message}")

l = Loger()
l.log("This is an info message")  
l.log("This is a warning message", "warning")
l.log("This is an error message", "error")
l.log("This is an unknown type message", "unknown")
