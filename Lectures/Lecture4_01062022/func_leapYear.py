def is_leap(year):
    # If a year is multiple of 400,
    # then it is a leap year
    if (year % 400 == 0):
        return True
 
    # Else If a year is multiple of 100,
    # then it is not a leap year
    if (year % 100 == 0):
        return False
 
    # Else If a year is multiple of 4,
    # then it is a leap year
    if (year % 4 == 0):
        return True

    return False
print(is_leap(400))
print(is_leap(300))
