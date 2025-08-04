def SumOfDigits(num):
    sum=0
    while num>0:
        a=num%10
        sum=sum+a
        num=num//10
    print(sum)

num=int(input("Enter the 2 digit num: "))
SumOfDigits(num)
    







num=int(input("Enter the number: "))
SumOfDigits(num)
print(num)