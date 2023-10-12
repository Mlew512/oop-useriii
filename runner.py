# Import and create your users here

from users.PremiumUser import PremiumUser
from users.FreeUser import FreeUser

#def __init__(self, email_address, drivers_license_number,str);

user_one = FreeUser("mclovin", "mclovin@student.edu", 190293)
user_two = PremiumUser("julia", "julia@amazing.org", 198735)


while True:

    user_one.create_post()
    user_two.create_post()
