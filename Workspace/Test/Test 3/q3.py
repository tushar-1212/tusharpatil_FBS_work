#WAP for calculting total salary
n=int(input("enter the no. of employees: "))
total_salary=0
emp=1

while emp<=n:
    salary=int(input("enter basic salary" + str(emp)+":"))
    if salary < 20000:
        da= salary* 0.10
        ta= salary* 0.12
        hra= salary* 0.15
    else:
        da= salary* 0.15
        ta= salary* 0.18
        hra= salary* 0.20

    total= salary+ da+ta+hra 
    print("total salary of employee",emp,":",total)
    total_salary+= total
    emp += 1

print("total salary of all employees:", total_salary)

