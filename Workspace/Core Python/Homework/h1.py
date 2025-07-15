num = int(input("Enter a number (0 to exit): "))

while num != 0:
    if num % 5 == 0:
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 5")
    
    num = int(input("Enter another number (0 to exit): "))

print("Program ended.")