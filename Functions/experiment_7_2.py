#Write a Python function that takes a positive integer and returns the sum of the 
#cube of all the positive integers smaller than the specified number.  
def sum_of_cubes():  
    try:  
        n = int(input("Enter a positive integer: "))  
        if n <= 0:  
            print("Invalid input. Please enter a positive integer.")  
            return  
        k = n - 1  
        result = (k * (k + 1) // 2) ** 2  
        print("The sum of cubes is:", result)  
    except ValueError:  
        print("Invalid input. Please enter a valid integer.")  
sum_of_cubes()  