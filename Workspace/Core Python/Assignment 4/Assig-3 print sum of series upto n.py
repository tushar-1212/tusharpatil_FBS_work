#print sum of series upto n

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of the series up to", n, "is:", sum)

