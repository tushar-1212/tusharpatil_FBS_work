# Write a program to print prime numbers between 1 to 100

for num in range(1, 101):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')