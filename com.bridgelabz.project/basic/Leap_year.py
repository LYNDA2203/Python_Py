year=int(input("Enter the year(4-digit):"))
if year < 1000:
    print("Please ensure you have entered the 4-digit number")
    
else:
    if (year % 4 == 0) and (year % 100 !=0  or year % 400 == 0):
        print (f"{year} is leap year")
    else:
        print(f"{year} is not a leap year")
        