#8.Print the gradesheet of a student for the given range of cgpa.Scan marks of five subjects and calculate the %age.
name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")
sap_id = input("Enter the SAP ID: ")
semester = input("Enter the semester: ")
course = input("Enter the course: ")

print("\nEnter marks for 5 subjects:")
subjects = ["PDS", "Python", "Chemistry", "English", "Physics"]
marks = []

for subject in subjects:
    score = int(input(f"{subject}: "))
    marks.append(score)
    
total_marks = sum(marks)
percentage = (total_marks / 500) * 100  
cgpa = percentage / 10  

if 0 <= cgpa <= 3.4:
    grade = "F"
elif 3.5 <= cgpa <= 5.0:
    grade = "C+"
elif 5.1 <= cgpa <= 6.0:
    grade = "B"
elif 6.1 <= cgpa <= 7.0:
    grade = "B+"
elif 7.1 <= cgpa <= 8.0:
    grade = "A"
elif 8.1 <= cgpa <= 9.0:
    grade = "A+"
elif 9.1 <= cgpa <= 10.0:
    grade = "O (Outstanding)"
else:
    grade = "Invalid CGPA"

print("\nGradesheet")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}   SAPID: {sap_id}")
print(f"Sem: {semester}      Course: {course}")
print("\nSubject name: Marks")
for i in range(5):
    print(f"{subjects[i]}:   {marks[i]}")
print(f"Percentage: {percentage:.2f}%")
print(f"CGPA: {cgpa:.1f}")
print(f"Grade: {grade}")
