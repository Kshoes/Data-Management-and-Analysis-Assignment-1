# mydate.py

import random

def is_valid_month_num(n):
    if n > 0 and n < 13:
        return True
    else:
        return False

def month_num_to_string(month_num):
    switcher = {
        1: "January",
        2: "February", 
        3: "March", 
        4: "April", 
        5: "May", 
        6: "June", 
        7: "July",
        8: "August", 
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(month_num)

def date_to_string(date_list):
    month = month_num_to_string(date_list[1])
    return month + " " + str(date_list[2]) + ", " + str(date_list[0])

def dates_to_strings(list_of_date_lists):
    strings = []
    for dates in list_of_date_lists:
        strings.append(date_to_string(dates))
    return strings

def remove_years(list_of_date_lists):
    removed_years = []
    for dates in list_of_date_lists:
        dates.pop(0)
        removed_years.append(dates)
    return removed_years

def is_leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_num_days_in_month(month_num, year):
    if month_num == 2 and is_leap_year(year):
        return 29
    else:
        switcher = {
            1: 31,
            2: 28, 
            3: 31, 
            4: 30, 
            5: 31, 
            6: 30, 
            7: 31,
            8: 31, 
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        return switcher.get(month_num)

def generate_date(start_year, end_year):
    date = []
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, get_num_days_in_month(month, year))
    date.append(year)
    date.append(month)
    date.append(day)
    return date




If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
The year is a leap year (it has 366 days).
The year is not a leap year (it has 365 days).