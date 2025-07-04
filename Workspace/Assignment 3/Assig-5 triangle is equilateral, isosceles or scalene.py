#to check whether the triangle is equilateral, isosceles or scalene.

s1 = float(input("Enter the first side of triangle: "))
s2 = float(input("Enter the second side of triangle: "))
s3 = float(input("Enter the third side of triangle: "))

if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    if s1 == s2 == s3:
        print("The triangle is equilateral")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")