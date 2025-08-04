#Write a program to remove all occurrences of a given element in the list.# Read list elements from the user
n=int(input("Enter the number of elements: "))
numbers=[]

for i in range(n):
    numbers += [int(input("Enter element: "))]
ele = int(input("Enter element to remove: "))
result = []
for x in numbers:
    if x != ele:
        result += [x]   
print(result)