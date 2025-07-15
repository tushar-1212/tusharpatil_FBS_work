number = int(input("Enter a number (0 to exit): "))

while number != 0:
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
    
    number = int(input("Enter another number (0 to exit): "))

print("Program ended.")