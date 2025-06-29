# To find the roots of a given quadratic equations

a=int(input("enter the value of a:"))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c:"))

ans= (b*b) - (4*a*c)
ans= ans ** 0.5
Root1= (-b+ ans ) / (2*a)
Root2= (-b- ans ) / (2*a)
print("Root 1:",Root1)
print("Root 2:",Root2)

