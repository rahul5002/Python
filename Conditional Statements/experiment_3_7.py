#7. Write a program which takes any date as input and display next date of the calendar 
day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True
else:
    leap_year = False

if month in [1, 3, 5, 7, 8, 10, 12]: 
    days_in_month = 31
elif month in [4, 6, 9, 11]: 
    days_in_month = 30
elif month == 2:  
    if leap_year:
        days_in_month = 29
    else:
        days_in_month = 28
else:
    print("Invalid month!")
    exit()

if day < days_in_month:
    day += 1
elif day == days_in_month:
    day = 1
    if month == 12:  
        month = 1
        year += 1
    else:
        month += 1
else:
    print("Invalid day!")
    exit()

print(f"The next date is: {day:02}-{month:02}-{year}")
