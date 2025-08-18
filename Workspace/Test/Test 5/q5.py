
list1 = [1, 2, 6, 8, 3, 5, 7, 4, 2]
list2 = [2, 5, 4, 6, 8, 6, 7, 1, 9]
list3 = []

for i in list1:
    if i not in list3:
        list3.append(i)


for j in list2:
    if j not in list3:
        list3.append(j)

print("Union lists:", list3)
