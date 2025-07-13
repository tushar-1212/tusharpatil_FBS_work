#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full (use loop)

ticket_price = float(input("Enter ticket price: "))
total_amount = 0

for i in range(1, 6):
    age = int(input("Enter age of person: "))
    if age < 12:
        total_amount += ticket_price * 0.7  # 30% discount
    elif age > 59:
        total_amount += ticket_price * 0.5  # 50% discount
    else:
        total_amount += ticket_price        # full price

print("Total amount to be paid for all five persons is:", total_amount)