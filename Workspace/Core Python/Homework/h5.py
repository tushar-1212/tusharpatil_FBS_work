year = int(input("Enter a year (0 to exit): "))

while year != 0:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
    
    year = int(input("Enter another year (0 to exit): "))

print("Program ended.")
