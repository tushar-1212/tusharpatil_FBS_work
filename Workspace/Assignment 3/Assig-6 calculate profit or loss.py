#a program to calculate profit or loss.

cost_price = float(input("Enter the cost price of the item: "))
selling_price = float(input("Enter the selling price of the item: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print("profit is:", profit_percentage)

elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print("loss is:", loss_percentage)

