# Positions on a chess board are identified by a letter and a number.
# Usually, the letter identifies the column, while the number identifies the row.
# Write a program that reads a position from the user.
# The program should determine if the column begins with a black square or a white square.
# Then use modular arithmetic (check if you know this concept) to report the color of the square in that row.

# Criteria:
# Your program may assume that a valid position will always be entered
# Input examples:
# Position: D5
# Position: A1
# Output examples:
# White
# Black

chessboard_color = input("Position: ")
column = chessboard_color[0]
row = int(chessboard_color[1])

if column in "ACEG":
    if row % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    if row % 2 == 0:
        print("Black")
    else:
        print("White")
    
# Solution:
# chessboard_color = input("Position: ")
