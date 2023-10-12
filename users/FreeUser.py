from .user import User

class FreeUser(User):
    
    def __init__(self, name, email_address, drivers_license_number):
        super().__init__(name,  email_address, drivers_license_number)
        self._post = 0


    @property
    def get_post(self):
        return self._post
            
    # Your PremiumUser class goes here
    def create_post(self, post):
        if self._post < 2:
            User.post_counter += 1
            self._post += 1
            # post = input("what would you like to post? : ...")
            new_post = f"{self._name} : {post}"
            User.posts[User.post_counter] = new_post
            print(User.posts)
            print(f"You have {2 - self._post} post remaining.")
        else:
            print("You have reached your post limit, to increase upgrade to premium.")
        