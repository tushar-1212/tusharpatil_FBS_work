#WAP to check if given number is Perfect Number. 

n = int(input("Enter a number: "))

sum_of_divisors = 0

for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i
if sum_of_divisors == n:
    print(n, "is a Perfect Number") 

else:
    print(n, "is not a Perfect Number")

    