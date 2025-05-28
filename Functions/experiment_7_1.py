#Write a Python function to find the maximum and minimum numbers from a 
#sequence of numbers.  (Note: Do not use built-in functions.) 
def min_max():   
    try:  
        input_str = input("Enter a sequence of numbers separated by spaces: ")  
        numbers_str = input_str.split()  
        numbers = [float(num_str) for num_str in numbers_str] 
        if not numbers:  
            print("No numbers were entered.")  
            return  
        min = numbers[0]  
        max = numbers[0]  
        for number in numbers:  
            if number < min:  
                min = number  
            if number > max:  
                max = number  
        print("Minimum:", min)  
        print("Maximum:", max)  
    except ValueError:  
        print("Invalid input. Please enter numbers separated by spaces.")  
min_max()  
