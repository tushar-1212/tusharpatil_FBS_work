#write a funtion to which we pass a parameter and print factors of given number.
def factor(num): 
    for i in range(1,num+1):
        if num % i==0:
            print(i)
    return

num= int(input("Enter a number to find its factors: "))
factor(num)


        


