# WAP to check if given number Strong Number. 
# A Strong Number is a number whose sum of the factorials of its digits equals the number itself.


n = int(input("Enter a number: "))
num=n # Store the original number for final comparison
sum_of_factorials = 0  # Initialize sum of factorials
while n > 0:
    digit = n % 10  # Get the last digit
    factorial = 1   # Initialize factorial for the digit

    # Calculate factorial of the digit
    for i in range(1, digit + 1):
        factorial *= i

    n //= 10  # Remove the last digit from n

    sum_of_factorials += factorial  # Add the factorial to the sum

# Check if the sum of factorials equals the original number
if sum_of_factorials == num:
    print(num, "is a Strong Number")

else:
    print(num, "is not a Strong Number")



# line 12: 
# This part calculates the factorial of the current digit.
#for i in range(1, digit + 1): means the loop will go from 1 up to the digit itself.
#factorial *= i means multiply the current value of factorial by i each time.
#Example:
#If the digit is 4:

#The loop does: 1 × 2 × 3 × 4 = 24
#So, 4! (4 factorial) is 24.
#This code finds the factorial of each digit in the number.
    