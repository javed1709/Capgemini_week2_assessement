'''Write a scenario where a `UserAuthentication` interface contains `login()` and 
`logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.'''
from abc import ABC, abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged in with Google")

    def logout(self):
        print("Logged out from Google")

class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged in with Facebook")

    def logout(self):
        print("Logged out from Facebook")

google_auth = GoogleAuth()
google_auth.login()
google_auth.logout()

facebook_auth = FacebookAuth()
facebook_auth.login()
facebook_auth.logout()