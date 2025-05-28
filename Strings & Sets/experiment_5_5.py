#Given a string containing both upper and lower case alphabets. Write a Python 
#program to count the number of occurrences of each alphabet (case 
#insensitive) and display the same. 
def count_alphabets(input_string):
    input_string = input_string.lower()
    alphabet_count = {}
    for char in input_string:
        if char.isalpha(): 
            alphabet_count[char] = alphabet_count.get(char, 0) + 1

    for char, count in sorted(alphabet_count.items()):
        print(f"{count}{char.upper()}")

user_input = input("Enter a string: ")
count_alphabets(user_input)
