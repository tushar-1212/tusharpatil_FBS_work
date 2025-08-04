list1=[]
c=int(input("Enter number of elements: "))
for i in range(c):
    list1+=[int(input("Enter elements: "))]


m=int(input("Enter first divisor: "))
n=int(input("Enter second divisor: "))
print(f"Numbers divisible by{m}and{n}: ")
for num in list1:
    if num % m == 0 and num % n == 0:
        print(num)


