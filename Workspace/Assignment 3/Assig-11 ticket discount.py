#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

a1 = int(input("Enter age of person 1: "))
a2 = int(input("Enter age of person 2: "))
a3 = int(input("Enter age of person 3: "))
a4 = int(input("Enter age of person 4: "))
a5 = int(input("Enter age of person 5: "))

ticket_price = float(input("Enter ticket price: "))
total_amount = 0

if a1 < 12:
    total_amount += ticket_price * 0.7  # 30% discount  
elif a1 > 59:
    total_amount += ticket_price * 0.5
else:
    total_amount += ticket_price
if a2 < 12:
    total_amount += ticket_price * 0.7  # 30% discount
elif a2 > 59:
    total_amount += ticket_price * 0.5  
else:
    total_amount += ticket_price
if a3 < 12:
    total_amount += ticket_price * 0.7  # 30% discount
elif a3 > 59:
    total_amount += ticket_price * 0.5
else:   
    total_amount += ticket_price    
if a4 < 12:
    total_amount += ticket_price * 0.7  # 30% discount
elif a4 > 59:
    total_amount += ticket_price * 0.5      
else:
    total_amount += ticket_price
if a5 < 12: 
    total_amount += ticket_price * 0.7  # 30% discount
elif a5 > 59:
    total_amount += ticket_price * 0.5
else:
    total_amount += ticket_price    

print("Total amount to be paid for all five persons is: ", total_amount)