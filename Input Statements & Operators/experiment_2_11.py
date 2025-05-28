#11. Write a program to find left shift and right shift values of a given number. 
n=int(input("Enter a number:"))
shift=int(input("Enter the number of position shifts you want:"))
left_shift=(n<<shift)
right_shift=(n>>shift)
print("Number after left shift is:",left_shift)
print("Number after left shift is:",right_shift)

