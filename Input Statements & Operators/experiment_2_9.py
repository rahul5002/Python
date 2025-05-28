#9. Write a program to find sum of first n natural numbers. 

n=int(input("Enter the no. of natural elements you want the sum for: "))
if (n<0):
    print("Invalid Input.")
else:
    sum=(n*(n+1))/2
    print(sum)