# 3 digit number, if first digit is doubled of 2nd digit and half of third digit.

num= int(input("Enter a 3 digit number:"))

a= num % 10
num=num // 10
c= num % 10 
d= num //10

print("first digit:",d)
print("second digit:",c)
print("third digit:",a)


if d == 2 * c and d == a / 2:
    print("Yes you have done it")
else:
    print("Please try next time")


