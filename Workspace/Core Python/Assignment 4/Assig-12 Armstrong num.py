# to print Armstrong number within a given range

start= int(input("Enter the start of the range: "))
end= int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    temp = num
    count = 0
    
    # Count the number of digits
    while temp != 0:
        a = temp % 10
        temp = temp // 10
        count += 1

    temp = num
    sum = 0
    
    # Calculate the sum of the digits raised to the power of count
    while temp != 0:
        a = temp % 10
        temp = temp // 10
        sum += (a ** count)

    # Check if the sum equals the original number
    if sum == num:
        print(num, "is an Armstrong number")








