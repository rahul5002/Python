#3. Find the greatest among two numbers. If numbers are equal than print CGPA=percentage/10 
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
if (x==y):
    print("CGPA=percentage/10 ")
elif (x>y):
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")