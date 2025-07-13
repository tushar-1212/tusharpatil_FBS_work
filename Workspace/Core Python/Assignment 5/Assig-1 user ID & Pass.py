#Write a program to prompt user to enter userid and password. 
# If Id and  password is incorrect give him chance to re-enter the credentials.
#  Let him try 3  times. 
#After that program to terminate. 

user=input("Enter your user ID: ")
password=input("Enter your password: ")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    if user == "Tushar" and password == "#tp12":
        print("Access granted!")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Incorrect user ID or password. Please try again.")
            # Prompt for re-entry of credentials
        
            user = input("Re-enter your user ID: ")
            password = input("Re-enter your password: ")
        else:
            print("Access denied. Too many incorrect attempts.")