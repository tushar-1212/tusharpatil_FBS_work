list1=[]
c=int(input("Enter number of elements: "))
for i in range(c):
    list1+=[int(input("Enter elements: "))]


for i in list1:
    if i%2==0:
        list1.remove(i)
print(list1)
