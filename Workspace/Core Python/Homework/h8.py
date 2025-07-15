num1 = int(input("Enter the first number (0 to exit): "))
num2 = int(input("Enter the second number (0 to exit): "))

while num1 != 0 and num2 != 0:
    # Swapping using a third variable
    temp = num1
    num1 = num2
    num2 = temp

    print("The swapped numbers are:")
    print("First number:", num1)
    print("Second number:", num2)

    # Input for next swap
    num1 = int(input("Enter the first number (0 to exit): "))
    num2 = int(input("Enter the second number (0 to exit): "))

print("Program ended.")