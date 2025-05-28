#5. Store details of n movies in a dictionary by taking input from the user. Each 
#movie must store details like name,  year, director name, production cost, 
#collection made (earning) & perform the following :- 
#a) print all movie details 
#b) display name of movies released before 2015 
#c) print movies that made a profit. 
#d) print movies directed by a particular director. 
def create_movie_dict(n):  
    movie_dict = {}  
    for _ in range(n):  
        name = input("Enter the movie name: ")  
        year = int(input("Enter the release year: "))  
        director = input("Enter the director's name: ")  
        production_cost = float(input("Enter the production cost: "))  
        collection_made = float(input("Enter the collection made: "))  
        
        movie_dict[name] = {  
            'year': year,  
            'director': director,  
            'production_cost': production_cost,  
            'collection_made': collection_made  
        }  
        
    return movie_dict  

def print_all_movies(movie_dict):  
    print("\nAll Movie Details:")  
    for name, details in movie_dict.items():  
        print(f"{name}: {details}")  

def movies_before_2015(movie_dict):  
    print("\nMovies Released Before 2015:")  
    for name, details in movie_dict.items():  
        if details['year'] < 2015:  
            print(name)  

def profitable_movies(movie_dict):  
    print("\nMovies That Made a Profit:")  
    for name, details in movie_dict.items():  
        if details['collection_made'] > details['production_cost']:  
            print(name)  

def movies_by_director(movie_dict, director_name):  
    print(f"\nMovies Directed by {director_name}:")  
    found = False  
    for name, details in movie_dict.items():  
        if details['director'].lower() == director_name.lower():  
            print(name)  
            found = True  
    if not found:  
        print(f"No movies found directed by {director_name}.")  

try:  
    n = int(input("Enter the number of movies: "))  
    if n <= 0:  
        print("Please enter a positive integer for the number of movies.")  
    else:  
        movie_dict = create_movie_dict(n)  

        print_all_movies(movie_dict)  
        movies_before_2015(movie_dict)  
        profitable_movies(movie_dict)  
        
        director_name = input("Enter the director's name to search for their movies: ")  
        movies_by_director(movie_dict, director_name)  
except ValueError:  
    print("Please enter valid numeric values.")