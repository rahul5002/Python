#Input two values from user where the first line contains N, the number of test cases. 
#The next N lines contain the space separated values of a and b. Perform integer division and print a/b. 
#Handle exception in case of ZeroDivisionError or ValueError. 
def division():
    try:
        test_cases = int(input("Enter number of test cases: "))
        for _ in range(test_cases):
            try:
                a, b = map(int, input("Enter two numbers (a b): ").split())
                print(f"Result: {a // b}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero")
            except ValueError:
                print("Error: Invalid input. Enter two integers.")
    except:
        print("Error: Invalid input. Enter two integers.")
division()