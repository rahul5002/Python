#Write a Python function to print 1 to n using recursion. (Note: Do not use loop) 
def recursion():  
    try:  
        n = int(input("Enter a positive integer: "))  
        if n <= 0:  
            print("Invalid input. Please enter a positive integer.")  
            return  
        def recursive_print(i):  
            if i > n:  
                return  
            print(i, end=" ")  
            recursive_print(i + 1)  
        recursive_print(1)  
        print()  
    except ValueError:  
        print("Invalid input. Please enter a valid integer.")  
recursion()  