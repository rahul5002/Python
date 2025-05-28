#4. WAP to enter a string and a substring. You have to print the number of times 
#that the substring occurs in the given string. String traversal will take place from 
#left to right, not from right to left. 

def count_substring(string, substring):
    count = 0
    start = 0
    while start < len(string):
        position = string.find(substring, start)
        if position == -1:
            break
        count += 1
        start = position + 1
    return count

main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
result = count_substring(main_string, substring)
print(f"The substring '{substring}' occurs {result} time(s) in the string '{main_string}'.")
