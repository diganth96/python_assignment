physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
biology = float(input("Enter Biology marks: "))
mathematics = float(input("Enter Mathematics marks: "))
computer = float(input("Enter Computer marks: "))
total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100
if percentage >= 90:
    grade = "Grade A"
elif percentage >= 80:
    grade = "Grade B"
elif percentage >= 70:
    grade = "Grade C"
elif percentage >= 60:
    grade = "Grade D"
elif percentage >= 40:
    grade = "Grade E"
else:
    grade = "Grade F"
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
