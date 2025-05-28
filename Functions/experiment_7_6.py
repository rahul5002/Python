#Write a lambda function which gives tuple of max and min from a list. 
# Lambda function to find the maximum and minimum elements in a list and return them as a tuple.  
find_tuple = lambda lst: (max(lst), min(lst)) if lst else (None, None)  
try:  
    input_str = input("Enter a list of numbers separated by spaces: ")  
    numbers = [float(x) for x in input_str.split()]   
    tuple = find_tuple(numbers)  
    if tuple == (None, None):  
        print("The list is empty.")  
    else:  
        print(f"The maximum and minimum values in the list are: {tuple}")  
except ValueError:  
    print("Invalid input. Please enter numbers separated by spaces.")  