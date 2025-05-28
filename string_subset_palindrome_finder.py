def find_longest_palindrome(string):
    if not string:
        return ""
    
    longest = string[0]
    
    for center in range(len(string)):
        left, right = center, center
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if right - left + 1 > len(longest):
                longest = string[left:right+1]
            left -= 1
            right += 1
        
        left, right = center, center + 1
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if right - left + 1 > len(longest):
                longest = string[left:right+1]
            left -= 1
            right += 1
    
    return longest

def main():
    print("Longest Palindromic Substring Finder")
    print("-----------------------------------")
    
    while True:
        user_input = input("\nEnter a string (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Thank you for using the palindrome finder!")
            break
        
        result = find_longest_palindrome(user_input)
        
        print(f"\nThe longest palindromic substring is: '{result}'")
        print(f"Length: {len(result)}")

if __name__ == "__main__":
    main()