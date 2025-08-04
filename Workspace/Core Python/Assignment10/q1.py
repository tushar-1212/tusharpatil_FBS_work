# Accept list size
n = int(input("Enter the number of elements: "))
numbers = []

# Accept elements one by one
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))    
    numbers.append(value)

# Calculate sum
total = 0
for num in numbers:
    total += num

print("Sum of all elements in the list is:", total)
