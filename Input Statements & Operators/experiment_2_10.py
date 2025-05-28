#10. Write a program to print truth table for bitwise operators( & , | and ^ operators) 

print("A\tB\tA&B\tA|B\tA^B")
print("-"*38)
for A in range(0,2):
    for B in range(0,2):
        and_operation=A&B
        or_operation=A|B
        xor_operation=A^B
        print(f"{A}\t{B}\t{and_operation}\t{or_operation}\t{xor_operation}")