#Write a program to create a duplicate of an existing list. It should not point to same list

n = int(input("Enter the number of elements: "))
original_list = []

# Taking input
for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    original_list += [element]  # Avoid using append()

# Manually create a duplicate list
duplicate_list = []
for i in range(len(original_list)):
    duplicate_list += [original_list[i]]

# Remove duplicates manually
unique_list = []
for i in range(len(duplicate_list)):
    found = False
    for j in range(len(unique_list)):
        if duplicate_list[i] == unique_list[j]:
            found = True
            break
    if not found:
        unique_list += [duplicate_list[i]]

# Display results
print("Original List:", original_list)
print("Duplicate List (after removing duplicates):", unique_list)