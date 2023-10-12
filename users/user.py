from abc import ABC, abstractmethod

class User(ABC):
    posts = {}
    post_counter = 0

    def __init__(
        self, name, email_address, drivers_license_number="unknown"
    ):
        self._name = name 
        self._email = email_address 
        self._dln = drivers_license_number  
        self._friends = 0

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def dln(self):
        return self._dln

    @property
    def friends(self):
        return self._friends

    def __str__(self):
        return f"{self.name}'s email is {self.email} and drivers license number is {self.dln}"

    @friends.setter 
    def set_friends(self, new_friends_number):
        if new_friends_number > 0:
            self._friends = new_friends_number
    @abstractmethod
    def create_post(self):
        pass

    @classmethod
    def delete_post(cls, post_number):
        for obj in cls.posts:
            if obj == post_number:
                cls.posts[post_number] = "deleted"
        print(cls.posts)


# user_1= User("tom", "tom@myspace.com", 2003030)
# mclovin = User("McLovin", "mclovin@hawaii.gov", 14787441)
# mclovin.create_post()
# user_1.create_post()
# # is using __str__ method
# # print(mclovin)#print of the self will use the string method
# # print(user_1)
# User.delete_post(1)
# # Your User class goes here
