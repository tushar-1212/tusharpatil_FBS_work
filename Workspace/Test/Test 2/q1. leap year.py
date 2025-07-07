# A program to accept year from the user and check its leap year or not .

year=int(input("Enter the year:"))

if year%4==0 and year%100!=0 or year%400==0:
    print("Its a leap year:",year)

else:
    print("Its not a leap year:",year)
