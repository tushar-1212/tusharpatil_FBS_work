#calculate selling price of book based on cost price and discount

cp= float(input("Enter cost price of book: "))
discount= float(input("Enter discount percentage: "))
sp= cp - (cp * discount / 100)
print("Selling price of book after discount is:", sp)
