from .user import User

class PremiumUser(User):
    
    def __init__(self, name, email_address, drivers_license_number):
        super().__init__(name,  email_address, drivers_license_number)
    # Your PremiumUser class goes here
    def create_post(self):
        User.post_counter += 1
        post = input("what would you like to post? : ...")
        new_post = f"{self._name} : {post}"
        User.posts[User.post_counter] = new_post
        print(User.posts)