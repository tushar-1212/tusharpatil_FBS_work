# To calculate the sum of a 3-digit number
num = int(input("Enter a 3-digit number: "))
a= num % 10
num=num // 10
c= num % 10 
d= num //10
sum= a + c + d
print("Sum of the digits of your 3-digit number is:", sum)
