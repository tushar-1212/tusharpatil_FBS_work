# WAP to calculate the sum of series 
# 1/1!+2/2!+.......+n/n!

n=int(input("Enter the end number: "))
sum=0
for i in range(1, n + 1):
    factorial= 1

    for j in range(1,i+ 1):
        factorial *= j
    sum += i/factorial
print("sum of serie: ",sum)
