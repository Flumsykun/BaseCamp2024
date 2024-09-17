# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type of the triangle.

# Criteria:
# Input is given as a comma seperated string: a=5, b=6, c=5
# All 3 sides of an equilateral triangle have the same length.
# An isosceles triangle has two sides that are the same length, and a third side that is a different length.
# If all of the sides have different lengths then the triangle is scalene.
# Input example:
# Sides: a=5, b=6, c=5

# Output example:
# Isosceles triangle

triangle_type_checker = input("Sides:")

# if triangle_type_checker[2] == triangle_type_checker[6] == triangle_type_checker[10]:
#     print("Equilateral triangle")
# elif triangle_type_checker[2] == triangle_type_checker[6] or triangle_type_checker[2] == triangle_type_checker[10] or triangle_type_checker[6] == triangle_type_checker[10]:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

sides = triangle_type_checker.split(", ")
a = int(sides[0][2:])
b = int(sides[1][2:])
c = int(sides[2][2:])

if a == b == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    
    