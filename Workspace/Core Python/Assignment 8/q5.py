def primeNum(num):
    sum=0
    for num in range(1,num+1):
        for i in range(2,num):
            if (num % i ==0):
                break
        else:
            sum=sum+num

    return f"sum of prime numbers {sum}"
    


num=int(input("enter the number:"))
result=primeNum(num)
print(result)
