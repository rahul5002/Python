#1. Write a program to count and display the number of capital letters in a given string. 
def count_capital_letters(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            count += 1
    return count

user_input = input("Enter a string: ")
capital_count = count_capital_letters(user_input)
print(f"The number of capital letters in the given string is: {capital_count}")
