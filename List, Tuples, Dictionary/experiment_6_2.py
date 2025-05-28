#2. Create a tuple to store n numeric values and find average of all values. 
# Function to calculate the average of values in a tuple  
def calculate_average(values):  
    if len(values) == 0:  
        return 0   
    return sum(values) / len(values)  

try:  
    n = int(input("Enter the number of numeric values: "))  
    if n <= 0:  
        print("Please enter a positive integer.")  
    else:  
        numeric_values = []  
        for i in range(n):  
            value = float(input(f"Enter value {i + 1}: "))  
            numeric_values.append(value)  

        values_tuple = tuple(numeric_values)  

        average = calculate_average(values_tuple)  
        print(f"The average of the values {values_tuple} is: {average}")  

except ValueError:  
    print("Please enter a valid integer or numeric value.")