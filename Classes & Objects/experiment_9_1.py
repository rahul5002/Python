class Student:
    def set_details(self):
        self.name = input("Enter Student Name: ")
        self.sap_id = input("Enter SAP ID: ")
        self.marks = {
            "Physics": int(input("Enter Physics Marks: ")),
            "Chemistry": int(input("Enter Chemistry Marks: ")),
            "Maths": int(input("Enter Maths Marks: "))
        }
    def display(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
students = [Student() for _ in range(3)]
for student in students:
    student.set_details()
for student in students:
    student.display()
