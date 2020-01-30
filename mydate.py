# mydate.py

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

