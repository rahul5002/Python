#Add few names, one name in each row, in “name.txt file”. 
#a. Count no of names 
#b. Count all names starting with vowel 
#c. Find longest name 
def analyze_names(names):
    vowels = "AEIOUaeiou"
    return (
        len(names),
        sum(1 for name in names if name and name[0] in vowels),
        max(names, key=len)
    )
with open('my_file.txt', 'r') as file:
    names = [name.strip() for name in file]
total_names, vowel_names, longest_name = analyze_names(names)
print(f"Total names: {total_names}")
print(f"Names starting with vowel: {vowel_names}")
print(f"Longest name: {longest_name}")