def sumofSeries(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return f"The sum of the series up to is {sum}"

def fact(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return f"The factorial of is {factorial}"

def powerOfnum(num):
    power=0
    for i in range(1,num+1):
        power+=i**i 
    return f"The power of a number is {power}"

num=int(input("enter the last number - n:"))
result=sumofSeries(num)
print(result)

result=fact(num)
print(result)

result=powerOfnum(num)
print(result)
