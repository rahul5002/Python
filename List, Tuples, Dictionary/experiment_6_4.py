#4. Create a dictionary of n persons where key is name and value is city.  
#a) Display all names 
#b) Display all city names 
#c) Display student name and city of all students. 
#d) Count number of students in each city. 
def create_student_dict(n):  
    student_dict = {}  
    for _ in range(n):  
        name = input("Enter the student name: ")  
        city = input("Enter the city: ")  
        student_dict[name] = city  
    return student_dict  

def display_names(student_dict):  
    print("All Names:")  
    for name in student_dict.keys():  
        print(name)  

def display_cities(student_dict):  
    print("All City Names:")  
    for city in set(student_dict.values()):  
        print(city)  

def display_students_and_cities(student_dict):  
    print("Student Name and City:")  
    for name, city in student_dict.items():  
        print(f"{name} - {city}")  

def count_students_in_cities(student_dict):  
    city_count = {}  
    for city in student_dict.values():  
        city_count[city] = city_count.get(city, 0) + 1  
    print("Number of Students in Each City:")  
    for city, count in city_count.items():  
        print(f"{city}: {count}")  

try:  
    n = int(input("Enter the number of students: "))  
    if n <= 0:  
        print("Please enter a positive integer for the number of students.")  
    else:  
        student_dict = create_student_dict(n)  

        display_names(student_dict)  
        display_cities(student_dict)  
        display_students_and_cities(student_dict)  
        count_students_in_cities(student_dict)  
except ValueError:  
    print("Please enter a valid integer.")