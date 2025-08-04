list1 = []
n = int(input("Enter number of elements: "))
print("Enter the elements :")
for _ in range(n):
    num = int(input())
    list1 += [num]   
result = []
for x in list1:
    if x % 2 != 0:
        result += [x] 
print("List after removing even numbers:", result)  