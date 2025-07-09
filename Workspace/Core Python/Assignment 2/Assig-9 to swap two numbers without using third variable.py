# to swap two numbers without using third variable.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1,num2 = num2, num1 

print("After swapping")
print("First number is:", num1)
print("Second number is:", num2)
