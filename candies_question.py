#There are n children standing in a line. Each child is assigned a rating value given in the integer array 
#ratings. You are giving candies to these children subjected to the following requirements:Each child
# must receive at least one candy. Children with higher ratings receive more candies than their peers.
#Return the minimum number of candies you must have to give away.
def min_candies(ratings):  
    n = len(ratings)  
    if n == 0:  
        return 0, []   
    
    candies = [1] * n 
    
    for i in range(1, n):  
        if ratings[i] > ratings[i - 1]:  
            candies[i] = candies[i - 1] + 1  
    
    for i in range(n - 2, -1, -1):  
        if ratings[i] > ratings[i + 1]:  
            candies[i] = max(candies[i], candies[i + 1] + 1)   
             
    return sum(candies), candies  

def get_user_ratings():  
    ratings_str = input("Enter the ratings for the children separated by spaces: ")  
    ratings = list(map(int, ratings_str.split()))  
    return ratings  

if __name__ == "__main__":  
    ratings = get_user_ratings()  
    total_candies, candies = min_candies(ratings)  
    print(f"The minimum number of candies required: {total_candies}")  
    print(f"Candies distributed to each child: {candies}")



                            
                                
                                         