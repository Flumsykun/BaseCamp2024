# Write a program that draws “modular rectangles” like the ones below.
# The user specifies the width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from left to right and top to bottom, but are all done mod 10.

# Input example:
# Width: 5
# Height: 3

# Output example:
# 0 1 2 3 4
# 5 6 7 8 9
# 0 1 2 3 4

input_width = int(input("Width: "))
input_height = int(input("Height: "))

for i in range(input_height):
    # Outer loop: iterates over each row (from 0 to input_height - 1)
    for j in range(input_width):
        # Inner loop: iterates over each column in the current row (from 0 to input_width - 1)
        print((i * input_width + j) % 10, end=" ")
        # (i * input_width + j) calculates the sequential number for the current cell
        # % 10 takes the remainder when the number is divided by 10, ensuring the value is between 0 and 9
        # end=" " ensures that the values are printed on the same line separated by a space
    print()
        # After finishing the inner loop, print() moves to the next line for the next row