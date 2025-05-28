#13. Using membership operator find whether a given character is in a string. 

string=input("Enter a string: ")
char=input("Enter the character you want to search in the string: ")
if (char in string):
    print(f"{char} is present in the sequence.")
else:
    print(f"{char} is not present in the sequence.")