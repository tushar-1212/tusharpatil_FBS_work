#WAP to print all odd numbers until n

n=int(input("Enter a number till you want odd numbers: "))
for i in range(1, n + 1):
    if i % 2 !=0:
        print(i)
