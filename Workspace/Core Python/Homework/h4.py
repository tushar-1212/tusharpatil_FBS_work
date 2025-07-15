temp = float(input("Enter temperature in Celsius (999 to exit): "))

while temp != 999:
    if temp <= 0:
        print("Below freezing point.")
    else:
        print("Above freezing point.")
    
    temp = float(input("Enter another temperature (999 to exit): "))

print("Program ended.")