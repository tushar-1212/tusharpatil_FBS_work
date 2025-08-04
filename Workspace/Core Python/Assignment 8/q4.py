def sumOdd(num):
    sum=0
    for i in range(1,num+1):
        if i % 2 != 0:
            sum += i
    return f"sum of all odd number- {sum} "
 
num=int(input("Enter the number: "))
result=sumOdd(num)
print(result)

