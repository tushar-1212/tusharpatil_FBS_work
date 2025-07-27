def count(num):
    if num != 0:
        return 1 + count(num // 10)
    else:
        return 0

def armstrong(num, n):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return (digit ** n) + armstrong(num // 10, n)

num = int(input("Enter the number: "))
c = count(num)
if num == armstrong(num, c):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

