from users.PremiumUser import PremiumUser
from users.FreeUser import FreeUser

#def __init__(self, email_address, drivers_license_number,str);

# user_one = FreeUser("mclovin", "mclovin@student.edu", 190293)
# user_two = PremiumUser("julia", "julia@amazing.org"

def test_add_post_free():
    user_one = FreeUser("mclovin", "mclovin@student.edu", 190293)
    assert user_one.create_post("testing test")
    assert user_one.create_post("testing test")
    #assert user_one.create_post("testing nothing") == "You have reached your post limit, to increase upgrade to premium."