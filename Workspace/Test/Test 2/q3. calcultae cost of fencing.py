
l=int(input("Enter length of the field: "))
b=int(input("Enter breadth of the field: "))
rad=int(input("Enter radius of the circular field: "))
r=int(input("Enter rate of fencing per meter: "))

perimeter= 2 * (l + b)+ 0.5 * 3.14 * rad * 5    # X5 times for field fencing
cost= perimeter * r 

print("Perimeter of the field is:", perimeter)
print("Cost of fencing the field is:", cost)
