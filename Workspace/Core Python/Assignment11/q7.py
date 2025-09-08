list1=[1,2,3,4,5,6,7]
list2=[2,3,6,9,10,11,13]

list1=list(map(int, list1))
list2=list(map(int, list2))

union_list= list1.copy()

for item in list2:
    if item in union_list:
        union_list.append(item)
    else:
        continue

print("Union of the two list: ",union_list)