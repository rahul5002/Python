#6. Write a program to print sum of digits. 
num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10  
    sum_of_digits += digit  
    num //= 10  

print(f"The sum of digits is: {sum_of_digits}")
