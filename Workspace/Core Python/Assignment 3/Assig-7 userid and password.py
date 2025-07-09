#to check if user has entered correct userid and password.

user= input("Enter your userid: ")
pass1= input("Enter your password: ")

if user == "admin" and pass1 == "@1234":
    print("Login successful")

else:
    print("Login failed, please try again")