#a program to input all sides of a triangle and check whether triangle is valid or not

s1=float(input("Enter the first side of triangle:"))
s2=float(input("Enter the second side of triangle:"))
s3=float(input("Enter the third side of triangle:"))

if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print("The triangle is valid")

else:
    print("Triangle is not valid")


