# birthday.py

import mydate

num_trials = input("How many times should I run the simulation?\n")
birthdays_per_trial = input("How many birthdays should I generate per trial?\n")

duplicate_dates_count = 0

for x in range(int(num_trials)):
    
    num_duplicates = 0
    new_dates = dict()
    duplicate_dates = set(())
    
    for y in range(int(birthdays_per_trial)):
        
        new_date = mydate.generate_date(1998, 1999)
        new_date.pop(0) # removing year
        # print(new_date)
        new_date = mydate.date_to_string(new_date)
        
        if new_date in new_dates:
            new_dates[new_date] += 1
            duplicate_dates.add(new_date)
            num_duplicates += 1
        else:
            new_dates[new_date] = 1
            
    dup_dates_string = ", ".join(x for x in duplicate_dates)
            
    trial_message = "Trial #{}: {} date(s) occurred more than once! {}"
    print(trial_message.format(x, num_duplicates, dup_dates_string))
    
    if len(duplicate_dates) != 0:
        duplicate_dates_count += 1

if(duplicate_dates_count == 0):
    percentage = 0
else:
    percentage = 100 * duplicate_dates_count/int(num_trials) 
results = "Results:\n====\nOut of {} trials, {} had dates that were repeated\nWe can conclude that you have a {}% chance of sharing a birthday with someone if you are in a group of {} people"
print(results.format(int(num_trials), duplicate_dates_count, percentage, int(birthdays_per_trial)))

