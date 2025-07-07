l=int(input("Enter length of the wall: "))
b=int(input("Enter breadth of the wall: "))
rate=int(input("Enter rate of paint per square meter: "))
area= l * b * 4  # 4 walls
paint_cost=area * rate

print("Area of the walls is:", area)
print("Cost of painting the walls is:", paint_cost)

