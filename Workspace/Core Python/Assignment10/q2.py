#Write a program to find maximum and minimum element in a list.

n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)

max_value = max(numbers)
min_value = min(numbers)
print("Maximum value in the list is:", max_value)
print("Minimum value in the list is:", min_value)
