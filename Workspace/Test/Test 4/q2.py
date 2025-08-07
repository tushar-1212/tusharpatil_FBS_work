#WAP a program to find factorial of all numbers in given range using a recursion.

def factorial(n):
    fact=1
    for i in range(1,n+1):
        if n == 0 or n == 1:
            return 1
        else:
            fact = n * factorial(n - 1)
    return 


    
n=int(input("Enter the number: "))
result=factorial(n)
print(result)



