#to find area and cost of painting for given wall

area_intwall=int(input("area of interior wall:")) #user has to give total area of his 4 walls 
area_extwall=int(input("area of exterior wall:")) #user has to give total area of his 4 walls
cost=int(input("cost of painting all walls:"))

total_area= area_extwall+area_intwall   
total_cost= total_area*cost

print("Total area of wall:",total_area)
print("Total cost of painting:",total_cost)
