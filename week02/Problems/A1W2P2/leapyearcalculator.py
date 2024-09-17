# Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that.
# As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years.
# Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.

# Criteria:
# Any year that is divisible by 400 is a leap year.
# Of the remaining years, any year that is divisible by 100 is not a leap year.
# Of the remaining years, any year that is divisible by 4 is a leap year.
# All other years are not leap years.
# Input examples:
# Year: 2012
# Year: 2011
# Output examples:
# Leap year
# Not a leap year

leap_year_calculator = int(input("Year:"))

if leap_year_calculator % 400 == 0:
    print("Leap year")
elif leap_year_calculator % 100 == 0:
    print("Not a leap year")
elif leap_year_calculator % 4 == 0:
    print("Leap year")
else:
    # print("Not a leap year")
    
    output = "Leap year" if leap_year_calculator % 400 == 0 or leap_year_calculator % 4 == 0 else "Not a leap year"
    print(output)
    