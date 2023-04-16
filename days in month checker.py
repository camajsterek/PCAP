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


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
