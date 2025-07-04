#a program to prompt user to enter userid and password. 
# After verifying userid and password display a 4 digit random number and ask user to enter the same. 
# If user enters the same number then show him success message otherwise failed. 

import random
user= input("Enter your userid: ")
pass1= input("Enter your password: ")

if user == "admin" and pass1 == "1234":
    captcha = random.randint(1000, 9999)
    print("Fill in the captcha to proceed:", captcha)
    user_captcha = int(input("Enter the captcha: "))
    if user_captcha != captcha:
        print("Captcha verification failed, please try again")
    else:
        print("Login successful")