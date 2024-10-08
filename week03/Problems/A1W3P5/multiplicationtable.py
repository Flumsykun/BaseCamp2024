# In this exercise you will create a program that displays a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10.

# Criteria:
# Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10.
# It should also include labels down the left side consisting of the numbers 1 through 10.
# Input:
# No input is given

# Output example:
#    1  2  3  4  5  6  7  8  9 10
# 1  1  2  3  4  5  6  7  8  9 10
# 2  2  4  6  8 10 12 14 16 18 20
# ...

#print the header row (numbers 1 through 10)
print("   ", end="") #print 3 spaces
for i in range(1, 11):
    print(f"{i:3}", end="") #print the number with 3 spaces
print() #print a newline

for row in range(1, 11):
    print(f"{row:2}", end="") #print the row number with 2 spaces
    for col in range(1, 11):
        print(f"{row * col:3}", end="") #print the product with 3 spaces
    print() #print a newline