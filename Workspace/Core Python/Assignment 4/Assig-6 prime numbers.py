# write a program for Prime number
num=int(input("enter the number:"))

for i in range(2,num):
    if (num % i ==0):
        print("Not a Prime Number")
        break

else:
    print("Prime Number")