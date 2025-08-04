#Write a program to find the second largest element in the list. 

n = int(input("Enter the number of elements: "))
numbers = []    

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)   


max= numbers [0]

sec_max = 0

for i in range(1,len(numbers)):
    if (max < numbers[i]):
        sec_max=max
        max=numbers[i]
    
    elif (sec_max < numbers[i]):
        sec_max=numbers[i]


print(sec_max)