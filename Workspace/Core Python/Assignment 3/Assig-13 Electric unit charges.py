#Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit - charges*0.50
#For next 100 units Rs. 0.75/unit - 
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit

charges =float(input("Enter electricity unit charges: "))
if charges <= 50:
    total_bill = charges * 0.50

elif charges <= 150:  #51-150 units
    total_bill = (50 * 0.50) + ((charges - 50) * 0.75)

elif charges <= 250:  #151-250 units
    total_bill = (50 * 0.50) + (100 * 0.75) + ((charges - 150) * 1.20) 

else: #above 250 units
    total_bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((charges - 250) * 1.50)

print("Total electricity bill is: Rs.", total_bill)


