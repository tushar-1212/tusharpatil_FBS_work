# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive function to calculate sum of factorials from 1! to n!
def sum_of_factorials(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_of_factorials(n - 1)


n = int(input("Enter a number: "))
result = sum_of_factorials(n)
print(f"Sum of series 1! + 2! + ... + {n}! is: {result}")
