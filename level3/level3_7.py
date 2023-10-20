# Input lists
students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

# Using dictionary comprehension to construct the dictionary
student_subjects = {students[i]: subjects[i] for i in range(len(students))}

# Print the resulting dictionary
print(student_subjects)
