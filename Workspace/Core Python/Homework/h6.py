num = int(input("Enter a number (0 to exit): "))

while num != 0:
    if num % 3 == 0:
        print("The number is a multiple of 3.")
    else:
        print("The number is not a multiple of 3.")
    
    num = int(input("Enter another number (0 to exit): "))

print("Program ended.")