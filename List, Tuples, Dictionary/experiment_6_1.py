#1.Scan n values in range 0-3 and print the number of times each value has occurred. 
def count_occurrences():  
    value_range = range(4)
    counts = {i: 0 for i in value_range}
 
    n = int(input("Enter the number of values to input: "))  

    print(f"Enter {n} values (0-3):")  
    for _ in range(n):  
        value = int(input())  
        if value in value_range:    
            counts[value] += 1    
        else:  
            print(f"Value {value} is out of range. Please enter a value between 0 and 3.")  

    print("Occurrences of each value:")  
    for value in value_range:  
        print(f"{value}: {counts[value]}")  

if __name__ == "__main__":  
    count_occurrences()