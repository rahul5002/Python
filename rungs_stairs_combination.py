from itertools import permutations  

def climb_stairs(n, steps, memo=None):  
    if memo is None:  
        memo = {}  

    if n == 0:  
        return 1, [steps]   
    
    if n < 0:  
        return 0, []  

    if n in memo:  
        return memo[n]  
    
    count_1, combinations_1 = climb_stairs(n - 1, steps + [1], memo)  
    count_2, combinations_2 = climb_stairs(n - 2, steps + [2], memo)  
    count_3, combinations_3 = climb_stairs(n - 3, steps + [3], memo)  

    total_count = count_1 + count_2 + count_3  
    
    all_combinations = combinations_1 + combinations_2 + combinations_3  
    
    unique_permutations = set(tuple(p) for combo in all_combinations for p in permutations(combo))  
    
    total_combinations = [list(perm) for perm in unique_permutations]  

    memo[n] = (total_count, total_combinations)  
    return total_count, total_combinations  

try:  
    rungs = int(input("Enter the number of rungs: "))  
    if rungs < 0:  
        print("The number of rungs cannot be negative.")  
    else:  
        count, combinations = climb_stairs(rungs, [])  
        print(f"The number of ways to climb {rungs} rungs is: {count}")  
        print("The combinations of steps are:")  
        
        for combo in combinations:  
            print(combo)  
        
except ValueError:  
    print("Please enter a valid integer.")