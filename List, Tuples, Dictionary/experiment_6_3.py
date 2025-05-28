#3. WAP to input a list of scores for N students in a list data type. Find the score of 
#the runner-up and print the output. 
def find_runner_up_score(scores):  
    unique_scores = list(set(scores))  
    
    unique_scores.sort(reverse=True)  
    
    if len(unique_scores) < 2:  
        return None  
    
    return unique_scores[1]  

try:  
    N = int(input("Enter the number of students: "))  
    
    scores = list(map(int, input(f"Enter the scores for {N} students (space-separated): ").split()))  
    
    if len(scores) != N:  
        print(f"Error: You must enter exactly {N} scores.")  
    else:  
        runner_up_score = find_runner_up_score(scores)  
        
        if runner_up_score is not None:  
            print(f"The runner-up score is: {runner_up_score}")  
        else:  
            print("There is no runner-up score (not enough unique scores).")  
except ValueError:  
    print("Please enter valid integer values.")