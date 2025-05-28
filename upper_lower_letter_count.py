def count_characters():
    string = input("Enter a string: ")
    upper_count = 0
    lower_count = 0
    space_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
            
    print(f"\nIn the string: '{string}'")
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")
    print(f"Spaces: {space_count}")
count_characters()