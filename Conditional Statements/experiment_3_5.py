#5. Check whether the quadratic equation has real roots or imaginary roots. Display the roots. 
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
D = b**2 - 4*a*c
if D > 0:
    print("The equation has two distinct real roots.")
    root1 = (-b + D**0.5) / (2 * a)
    root2 = (-b - D**0.5) / (2 * a)
    print(f"Roots: {root1}, {root2}")
elif D == 0:
    print("The equation has two equal real roots.")
    root = -b / (2 * a)
    print(f"Root: {root}")
else:
    print("The equation has two imaginary roots.")
    root1 = (-b + (D)**0.5) / (2 * a)
    root2 = (-b - (D)**0.5) / (2 * a)
    print(f"Roots: {root1}, {root2}")

