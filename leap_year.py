"Take a year and check whether it is leap year or not"

year = int(input("Enter a year : "))

if ((year% 400 == 0) or (year%4==0 and year %100!=0)):
    print(f"This {year} is leap year ")
else:
    print(f"This {year} is not leap year  ")
