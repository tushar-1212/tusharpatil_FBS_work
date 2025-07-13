x=int(input("Enter the number for x^n: "))
n=int(input("Enter the number for 2n-1:"))
sum=0

for i in range(1,n+1):
    term=(x**i)/(2*i)-1

    if (i % 2 == 0):
        sum -= term
    else:
        sum += term
