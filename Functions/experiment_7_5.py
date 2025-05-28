#Write a lambda function to find volume of cone. 
# Lambda function to calculate the volume of a cone  
volume_of_cone = lambda radius, height: (1/3) * 3.14159 * radius**2 * height  
try:  
    radius = float(input("Enter the radius of the cone: "))  
    height = float(input("Enter the height of the cone: "))  
    volume = volume_of_cone(radius, height)  
    print(f"The volume of the cone with radius {radius} and height {height} is: {volume}")  
except ValueError:  
    print("Invalid input. Please enter numeric values for radius and height.")  