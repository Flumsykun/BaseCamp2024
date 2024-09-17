# Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user and then report the appropriate name as part of a meaningful message.

# Criteria:
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
# If a number of sides outside of this range is entered then your program should display the error message: Amount of sides is out of range.
# Input examples:
# Sides: 3
# Sides: 4
# Output examples:
# Triangle
# Square

number_of_sides = int(input("Sides: "))

if number_of_sides == 3:
    print("Triangle")
elif number_of_sides == 4:
    print("Square")
elif number_of_sides == 5:
    print("Pentagon")
elif number_of_sides == 6:
    print("Hexagon")
elif number_of_sides == 7:
    print("Heptagon")
elif number_of_sides == 8:
    print("Octagon")
elif number_of_sides == 9:
    print("Nonagon")
elif number_of_sides == 10:
    print("Decagon")
else:
    print("Amount of sides is out of range")
    