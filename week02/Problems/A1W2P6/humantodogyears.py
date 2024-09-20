# It is commonly said that one human year is equivalent to 7 dog years.
# However this simple conversion fails to recognize that dogs reach adulthood in approximately two years.
# As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.
# Write a program that implements the conversion from human years to dog years described in the previous paragraph.

# Criteria:
# First 2 human years are 10.5 dog years per human year
# Each extra human year is 4 dog years per human year
# Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years
# Your program should display an error message Only positive numbers are allowed if the user enters a negative number
# Input examples:
# Human years: 1
# Human years: 4
# Human years: -1
# Output examples:
# Dog years: 10.5 
# Dog years: 29
# Only positive numbers are allowed

doggo_converter = int(input("Human years: "))
if doggo_converter < 0:
    print("Only positive numbers are allowed")
elif doggo_converter == 1:
    print("Dog years: 10.5")
elif doggo_converter == 2:
    print("Dog years: 21")
else:
    print("Dog years:", 21 + (doggo_converter - 2) * 4)
    