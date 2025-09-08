list1=[[2,22],[34,56],[21,87],[1, 5], [3, 2], [4, 8], [2, 1]]
n=len(list1)

for i in range(n):
    for j in range(0,n-i-1):
        if list1[j][1] > list1[j + 1][1]:
            
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)
