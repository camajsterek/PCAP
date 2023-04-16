def is_year_leap(year):
    # test if divisible by four
    if year % 4 != 0:
        return False
    # test if divisible by 100 and 400
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    # return for 31 day months
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # return for 30 day months
    elif month in [4, 6, 9, 11]:
        return 30
    # check if leap year
    elif is_year_leap(year) == False:
        return 28
    # return if leap year
    else:
        return 29


def day_of_year(year, month, day):
    # sanity check
    if month > 12:
        return None
    # sanity check
    elif day > days_in_month(year, month):
        return None
    # can't deal with pre-gregorian
    elif year < 1583:
        return None
    else:
        days = 0
        for i in range(0, month):
            days += days_in_month(year, i+1)
        return days


print(day_of_year(2000, 12, 31))
