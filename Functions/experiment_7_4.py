#Write a recursive function to print Fibonacci series upto n terms. 
def recursive_fibonacci():  
    try:  
        n = int(input("Enter a non-negative integer: "))  
        if n < 0:  
            print("Invalid input. Please enter a non-negative integer.")  
            return  
        def fibonacci(n):  
            if n <= 0:  
                return 0  
            elif n == 1:  
                return 1  
            else:  
                return fibonacci(n - 1) + fibonacci(n - 2)  
        for i in range(n):  
            print(fibonacci(i), end=" ")  
        print()  
    except ValueError:  
        print("Invalid input. Please enter a valid integer.")  
recursive_fibonacci()  