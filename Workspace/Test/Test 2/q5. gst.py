p1=float(input("Enter the price of the product: "))
p2=float(input("Enter the price of the product: ")) 
p3=float(input("Enter the price of the product: "))
p4=float(input("Enter the price of the product: "))
p5=float(input("Enter the price of the product: ")) 
gst_rate=0.18  # GST rate is 18%
total_price = p1 + p2 + p3 + p4 + p5
gst_amount = (total_price * gst_rate)
final_price = total_price + gst_amount
print("Total price of the products is:", final_price)