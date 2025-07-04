#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1 = float(input("Enter marks for subject 1: "))
s2 = float(input("Enter marks for subject 2: "))
s3 = float(input("Enter marks for subject 3: "))
s4 = float(input("Enter marks for subject 4: "))
s5 = float(input("Enter marks for subject 5: "))

total_marks = s1 + s2 + s3 + s4 + s5
average_marks = total_marks / 500 * 100                                      # percentage

if average_marks >=75 and average_marks <= 100:
    print("Grade= First Class with Distinction")
elif average_marks >= 60:
    print("Grade= First Class")
elif average_marks >= 50:
    print("Grade= Second Class")
elif average_marks >= 40:
    print("Grade= Third Class")
elif average_marks >= 0:
    print("Grade= Fail ")
else:
    print("Invalid marks entered.") 

print("Total Marks:",total_marks)
print("Average Marks:",average_marks)   







