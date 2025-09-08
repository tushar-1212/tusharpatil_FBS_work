n = int(input("Enter the number of elements: "))
numbers = []
list2=[]
list3=[]

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)

for i in numbers:
    list2.append(i**2)  # Calculate square of each number and append to list2

for i in numbers:
    list3.append(i**3) # calculates cube for each number and append to list 3

print("The list of numbers is:", numbers)
print("The list of squares is:", list2)
print("The list of cubes is:", list3)
