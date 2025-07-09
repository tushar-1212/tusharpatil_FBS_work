#a program to check if given 3 digit number is a palindrome or not
# A palindrome is a number that remains the same when its digits are reversed.

num = int(input("Enter a 3-digit number: "))
temp = num  # Store the original number for comparison later
a= num % 10
num=num // 10
b= num % 10 
reverse= (a*10) + b
c= num //10
reverse= (reverse * 10) + c

if reverse == temp:
    print("Your 3-digit number is a palindrome.")

else:
    print("Your 3-digit number is not a palindrome.")