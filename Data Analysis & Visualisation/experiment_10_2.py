import numpy as np
def analyze_user_array():
    arr = np.zeros((3, 3))
    print("Enter the elements for a 3x3 array:")
    for i in range(3):
        for j in range(3):
            arr[i][j] = float(input(f"Enter element at position ({i+1},{j+1}): "))
    
    print("\nYour 3x3 NumPy array:")
    print(arr)
    print("\n")
    row_sums = np.sum(arr, axis=1)
    print("Sum of each row:")
    for i, row_sum in enumerate(row_sums):
        print(f"Row {i+1}: {row_sum}")
    print("\n")
    column_sums = np.sum(arr, axis=0)
    print("Sum of each column:")
    for i, col_sum in enumerate(column_sums):
        print(f"Column {i+1}: {col_sum}")
    print("\n")
    flattened = arr.flatten()
    sorted_array = np.sort(flattened)[::-1]
    second_max = sorted_array[1]
    print(f"The 2nd maximum element in the array is: {second_max}")

analyze_user_array()