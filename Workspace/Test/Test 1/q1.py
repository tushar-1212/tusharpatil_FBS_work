#area and perimeter of given figure 

l=int(input("Enter the lenght:"))
b=int(input("Enter the breadth:"))
r=int(input("Enter the radius:"))

area_rec= l*b
area_scir= 1/2*3.14*r*r
total_area= area_rec+ area_scir

prim_rec= 2(l+b)
prim_scir= 2*3.14*r/2
total_prim= prim_rec+prim_scir

print("area of given figure:",total_area)
print("perimeter of given figure:",total_prim)
