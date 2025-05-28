#3. Print Fibonacci series up to given term. 
n = int(input("Enter the number of terms: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to 1 term: ", a)
else:
    print("Fibonacci sequence up to", n, "terms:")
    print(a, end=" ")  
    for i in range(1, n):
        print(b, end=" ")  
        a, b = b, a + b  
