x=1
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    x=j+1
    for j in range(1,i):
        print(x,end=" ")
        x+=1
    print()


#           1 
#         1 2 3 
#       1 2 3 4 5
#     1 2 3 4 5 6 7
#   1 2 3 4 5 6 7 8 9