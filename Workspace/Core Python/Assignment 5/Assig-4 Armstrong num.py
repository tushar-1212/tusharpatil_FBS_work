# Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter a number: "))
temp = num  
sum = 0
count = 0

while (num!=0):
    a=num%10
    num=num//10
    count +=1

num = temp  # Reset num to the original value
while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp //= 10
    
if sum == num:
    print(num, "is an Armstrong number.")   
else:
    print(num, "is not an Armstrong number.")


