#12. Using membership operator find whether a given number is in sequence (10,20,56,78,89) 
sequence = (10,20,56,78,89)
n = int(input("Enter the number you want to search: "))
if (n in sequence):
    print(f"{n} is present in the sequence.")
if (n not in sequence):
    print(f"{n} is not present in the sequence.")