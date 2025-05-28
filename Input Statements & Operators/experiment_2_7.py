#7. Write a program to convert given seconds into hours, minutes and remaining seconds. 

sec=int(input("Enter the time in seconds:"))
min=sec/60
hours=min//60
remaining_sec=(min/60)-(hours)
print(sec)
print(min)
print(hours)
print(remaining_sec)

