# WAP to calculate total salary of employee based on basic,
# da (dearness allowance)=10% of basic,ta (travel allowance)=12% of basic, hra (house rent allowance)=15% of basic 

basic_salary= float(input("Enter the basic salary of the employee: "))
 #calculate da
da = (10/100) * basic_salary

#calculate ta
ta = (12/100) * basic_salary

#calculate hra
hra = (15/100) * basic_salary

#calculate total salary
total_salary = basic_salary + da + ta + hra
print("Total salary of the employee is:", total_salary)



