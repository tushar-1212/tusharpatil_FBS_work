# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

N = int(input("Enter value of N: "))
sum = 0

for i in range(1, N+1):
    sum = sum + (N ** i)

print("Sum of power series:", sum)