#Enter number of students from user.
#  For those many students accept marks of 5 subject marks from user
#  and calculate percentage.
#  Display all percentage and average percentage of students. 

# 2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

students = int(input("Enter number of students: "))

total_percent = 0 

for i in range(1, students+1):
    print("\nEnter marks of 5 subjects for Student", i)
    total = 0

    for j in range(1, 6):

        marks = int(input("Enter marks for subject " + str(j) + ": "))
        total = total + marks
    percent = (total / 500) * 100

    print("Total marks of Student", i, "=", total)
    print("Percentage of Student", i, "=", percent)

    total_percent = total_percent + percent
    

average = total_percent / students
print("\nAverage Percentage of all students =", average)