# Input number of elements
n = int(input("Enter the number of elements: "))
numbers = []

# Collect elements from user
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)

# Remove duplicates using a new list
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Display result
print("List after removing duplicates:", unique_numbers)