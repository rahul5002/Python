#Write functions to explain mentioned concepts: 
#a. Keyword argument 
#b. Default argument 
#c. Variable length argument 
def keyword_argument(name, greeting="Hello"):  
    print(f"{greeting}, {name}!")  
def default_argument(name="Guest"):  
    print(f"Welcome, {name}!")  
def variable_length_argument(*args, **kwargs):  
    print("Positional arguments (args):", args)  
    print("Keyword arguments (kwargs):", kwargs)  
print("Demonstrating Keyword Arguments:")  
keyword_argument(name="Alice", greeting="Hi")  
print("\nDemonstrating Default Arguments:")  
default_argument()  
default_argument("Bob")  
print("\nDemonstrating Variable Length Arguments:")  
variable_length_argument(1, 2, 3, name="Alice", age=25)
