#program to find sum of digits using reccuring funtions
def sumOfdigits(num):
    if (num==0):
        return 0
    else:
        a=num %10
        return a+sumOfdigits(num//10)
    
num=int(input("Enter the your number: "))
print(sumOfdigits(num))