#Program to find minimum no.of notes for given amount
amount=int(input("enter the amount:"))
n500= amount //500
r_amount= amount % 500

n200= r_amount // 200
r_amount= r_amount % 200

n100= r_amount // 100
r_amount= r_amount % 100 

n50= r_amount // 50
r_amount= r_amount % 50

n20= r_amount // 20
r_amount= r_amount % 20

n10= r_amount // 10
r_amount= r_amount % 10


print("Notes to be paid for amount:", amount)
print("RS.500 notes : ",n500)
print("RS.200 notes : ",n200)
print("Rs.100 notes : ",n100)
print("Rs.50  notes : ",n50)
print("Rs.10  notes : ",n10)


