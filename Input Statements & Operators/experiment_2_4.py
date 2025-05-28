#4. Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.  

p=int (input("Enter the length of perpendicular:"))
b=int (input("Enter the length of base:"))
h=(p**2+b**2)**(1/2)
print("Hypotenuse of the right triangle is :",h)
