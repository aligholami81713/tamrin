def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return true 
    else:      
        return false

year = int(input("inter a year: "))
if is_leap_year(year):
    print(f"{year} true ")
else:
    print(f"{year} false ")
