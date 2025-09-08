# Function to separate even and odd elements
def separate_even_odd(numbers):
    even_list = []
    odd_list = []
    
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    return even_list, odd_list

input_list=[]
c=int(input("Enter number of elements: "))
for i in range(c):
    input_list+=[int(input("Enter elements: "))]

even, odd = separate_even_odd(input_list)

print("Even numbers:", even)
print("Odd numbers:", odd)
