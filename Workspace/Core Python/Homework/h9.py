age = int(input("Enter your age (0 to exit): "))

while age != 0:
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
    
    age = int(input("Enter your age (0 to exit): "))

print("Program ended.")