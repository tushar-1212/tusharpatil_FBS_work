# To covert given days into years,weeks & days.
days=int(input("Enter the number of days:"))
years= days//365
days=days%365
weeks=days//7
days=days%7
print("years:",years,"weeks:",weeks,"days:",days)