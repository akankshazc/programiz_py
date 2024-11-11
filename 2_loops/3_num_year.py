# Python function to calculate the number of leap years between two given years

def count_leap_years(year1, year2):
    count = 0
    for year in range(year1, year2 + 1):
        if (year % 400) == 0 and (year % 100) == 0:
            count += 1
        elif (year % 4) == 0 and (year % 100) != 0:
            count += 1
    return count
