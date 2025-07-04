#a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

age=int(input("Enter your age: "))
gender= input("Enter your gender (M/F): ")
              

if gender=="M" and age >= 21 and age <70:
    print("You are eligible to marry.")

if gender=="F" and age >= 18 and age <70:
    print("You are eligible to marry.") 

else:
    print("You are not eligible to marry.")

