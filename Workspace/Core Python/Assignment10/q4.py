#Write a program to reverse the list.

n=int(input("Enter number of elements: "))
numbers=[]


for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)  

reversed_numbers = numbers[::-1]
print("Reversed list:", reversed_numbers)
