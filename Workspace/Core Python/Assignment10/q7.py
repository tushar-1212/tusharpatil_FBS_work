# Write a program to create a new list from existing list which contains cube of each number of list.

n=int(input("Enter the number of elemenrt: "))
numbers=[]

for i in range(n):
    value=int(input("Enter the element: "))
    numbers.append(value)

cubes = []
for n in numbers:
    cubes.append(n ** 3)
print(cubes)