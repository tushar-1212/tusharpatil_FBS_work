amt = int(input("Enter the amount: "))
D = [2000, 500, 200, 100, 50, 20, 10]

for i in D:
    count = amt // i
    amt = amt %  i 
    print(f"Rs.{i} notes: {count}")
