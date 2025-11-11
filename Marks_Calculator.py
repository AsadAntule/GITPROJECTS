marks = []
marks1 = int(input("Enter marks for sub 1: "))
marks2 = int(input("Enter marks for sub 2: "))
marks3 = int(input("Enter marks for sub 3: "))
marks4 = int(input("Enter marks for sub 4: "))
marks5 = int(input("Enter marks for sub 5: "))
while marks1 < 0 or marks1 > 100:
    marks1 = int(input("Invalid input. Enter marks for sub 1 again: "))
while marks2 < 0 or marks2 > 100:
    marks2 = int(input("Invalid input. Enter marks for sub 2 again: "))
while marks3 < 0 or marks3 > 100:
    marks3 = int(input("Invalid input. Enter marks for sub 3 again: "))
while marks4 < 0 or marks4 > 100:
    marks4 = int(input("Invalid input. Enter marks for sub 4 again: "))
while marks5 < 0 or marks5 > 100:
    marks5 = int(input("Invalid input. Enter marks for sub 5 again: "))
total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100
print("Total Marks:", total_marks)
remarks = ""
if percentage >= 90:
    grade = "A+"
    remarks = "Excellent"
elif percentage >= 80:
    grade = "A"
    remarks = "Very Good"
elif percentage >= 70:
    grade = "B"
    remarks = "Good"
elif percentage >= 60:
    grade ="C"
    remarks = "Average"
elif percentage >= 50:
    grade = "D"
    remarks ="Pass"
else:
    grade = "F"
    remarks = "Fail"
print("Percentage:", percentage)
print("Grade:", grade)
print("Remarks:", remarks)

