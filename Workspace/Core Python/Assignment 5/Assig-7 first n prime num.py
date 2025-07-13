#Write a program to print first n prime numbers

n = int(input("Enter the number of prime numbers to print: "))
count = 0
num = 2  # Starting from the first prime number

while count < n:
    for i in range(2,num):
        if (num % i == 0):
            break
    else:
        print(num, end=' ')
        count += 1
    num += 1  # Move to the next number
print()  # For a new line after printing all prime numbers

