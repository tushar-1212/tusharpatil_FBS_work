for i in range(1,5):
    for j in range(1,6):
        if (i+j)%2==0:
            print("1",end="")
        else:
            print("0", end="")
    print()