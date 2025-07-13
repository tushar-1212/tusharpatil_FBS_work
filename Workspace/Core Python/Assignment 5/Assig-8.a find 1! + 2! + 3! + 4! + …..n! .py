#1! + 2! + 3! + 4! + …..n! 

n=int(input("Enter a number: "))
factorial = 1
sum_factorial = 0
for i in range(1, n + 1):
    factorial *= i
    for j in range(1, i + 1):
         factorial *= j
         
    sum_factorial += factorial
    factorial = 1 
print("The sum of factorials from 1 to", n, "is:", sum_factorial)

