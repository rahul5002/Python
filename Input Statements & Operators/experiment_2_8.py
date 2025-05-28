#8. Write a program to swap two numbers without taking additional variable. 

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("Old Value of 'a' is:",a)
print("Old Value of 'b' is:", b)

a = a + b  
b = a - b  
a = a - b  

print("New Value of 'a' is:",a)
print("New Value of 'b' is:", b)
