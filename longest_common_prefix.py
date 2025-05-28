def longest_common_prefix(st):  
    if not st:  
        return ""  
    
    prefix = st[0]  
    
    for string in st[1:]:  
        while string[:len(prefix)] != prefix and prefix:  
            prefix = prefix[:-1]  
    
    return prefix  

user_input = input("Enter an array of strings separated by spaces: ")  
st = user_input.split()  

result = longest_common_prefix(st)  
print("Longest common prefix:", result)