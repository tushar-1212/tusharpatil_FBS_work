# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
#  (Use looping to optimize the problem)

amount = int(input("Enter the amount: "))

notes = [500, 200, 100, 50, 20, 10]

print("Minimum number of notes:")

# Loop through each note denomination
for note in notes:
    if amount >= note:
        count = amount // note   # Number of notes of this denomination
        amount = amount % note   # Update the remaining amount
        print(str(note) + " : " + str(count))
        