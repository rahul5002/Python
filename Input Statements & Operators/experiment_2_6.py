#6. Write a program to find area of triangle when length of sides are given. 

s1=int(input("Enter the first side of triangle: "))
s2=int(input("Enter the second side of triangle: "))
s3=int(input("Enter the third side of triangle: "))
semi_perimeter=(s1+s2+s3)/2
s=((semi_perimeter-s1)*(semi_perimeter-s2)*(semi_perimeter-s3))**(1/2)
print(s)