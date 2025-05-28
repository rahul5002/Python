class Student:
    def __init__(self, name, sap_id, physics, chemistry, mathematics):
        self.name = name
        self.sap_id = sap_id
        self.physics = physics
        self.chemistry = chemistry
        self.mathematics = mathematics
    
    def display(self):
        print(f"\nName: {self.name}, SAP ID: {self.sap_id}")
        print(f"Marks - Physics: {self.physics}, Chemistry: {self.chemistry}, Mathematics: {self.mathematics}")
    
    def marks_percentage(self):
        return (self.physics + self.chemistry + self.mathematics) / 3
    
    def display_result(self):
        percentage = self.marks_percentage()
        result = "PASS" if (self.physics >= 40 and self.chemistry >= 40 and self.mathematics >= 40) else "FAIL"
        print(f"Percentage: {percentage:.2f}%, Result: {result}")
        
def calculate_class_average(students):
    if not students:
        return 0
    
    total_percentage = sum(student.marks_percentage() for student in students)
    return total_percentage / len(students)

n = int(input("Enter number of students: "))
students = []
for i in range(n):
    print(f"\nStudent {i+1}:")
    name = input("Name: ")
    sap_id = input("SAP ID: ")
    physics = float(input("Physics marks: "))
    chemistry = float(input("Chemistry marks: "))
    mathematics = float(input("Mathematics marks: "))
    students.append(Student(name, sap_id, physics, chemistry, mathematics))
print("\n----- STUDENT RESULTS -----")
for i, student in enumerate(students):
    print(f"\nStudent {i+1}:")
    student.display()
    student.display_result()
    
class_average = calculate_class_average(students)
print(f"\n----- CLASS STATISTICS -----")
print(f"Class Average: {class_average:.2f}%")
if students:
    highest_student = max(students, key=lambda student: student.marks_percentage())
    lowest_student = min(students, key=lambda student: student.marks_percentage())
    print(f"Highest Percentage: {highest_student.name} ({highest_student.marks_percentage():.2f}%)")
    print(f"Lowest Percentage: {lowest_student.name} ({lowest_student.marks_percentage():.2f}%)")