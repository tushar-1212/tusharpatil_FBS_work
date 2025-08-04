#Accept a number from user and check if this element is present in the list or not.
#  Also tell how many times it is present in the list.

n=int(input("Enter the number of elements: "))
numbers=[]

for i in range(n):
    value=int(input(f"Enter the element {i+1}: "))
    numbers.append(value)
   


count = 0
element = int(input("Enter element to search: "))
for x in numbers:
    if x == element:
        count += 1

if count > 0:
    print("Yes, present")
    print("Count:", count)
else:
    print("No, not present")