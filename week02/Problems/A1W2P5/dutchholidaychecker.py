# Write a program that reads a month and day from the user.
# If the month and day match one of the Dutch national holidays then your program should display the holiday’s name.
# Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.

# Criteria:
# Input is given as a comma seperated string: Month: 12, Day: 5
# If no holiday is found, print error message: No holiday found on given input
# Input example:
# Date: Month: 12, Day: 5

# Output example:
# Sinterklaas

dutch_holiday_checker = input("Date: ") # Month: xx, Day: xx

if dutch_holiday_checker == "Month: 1, Day: 1":
    print("New Year's Day")
elif dutch_holiday_checker == "Month: 4, Day: 27":
    print("King's Day")
elif dutch_holiday_checker == "Month: 5, Day: 4":
    print("Remembrance Day")
elif dutch_holiday_checker == "Month: 5, Day: 5":
    print("Liberation Day")
elif dutch_holiday_checker == "Month: 12, Day: 5":
    print("Sinterklaas")
elif dutch_holiday_checker == "Month: 12, Day: 25":
    
else:
    print("No holiday found on given input")
    