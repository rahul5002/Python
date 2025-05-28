import numpy as np

def matrix_multiplication():
    n = int(input("Enter the size of the matrices (n for n×n matrices): "))
    matrix1 = np.zeros((n, n))
    matrix2 = np.zeros((n, n))    
    print("\nEnter elements for first matrix:")
    for i in range(n):
        for j in range(n):
            matrix1[i][j] = float(input(f"Enter element at position ({i+1},{j+1}): "))
    
    print("\nEnter elements for second matrix:")
    for i in range(n):
        for j in range(n):
            matrix2[i][j] = float(input(f"Enter element at position ({i+1},{j+1}): "))
    
    print("\nFirst Matrix:")
    print(matrix1)
    print("\nSecond Matrix:")
    print(matrix2)
    result = np.dot(matrix1, matrix2)
    print("\nMatrix Multiplication Result:")
    print(result)

matrix_multiplication()

# Alternative way: using the @ operator (Python 3.5+)
    # result = matrix1 @ matrix2