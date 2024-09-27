# Do some research regarding truth tables.
# Use iterative programming to solve this problem to print the truth tables for and and or.
# Implement a program that prints these two truth tables.

# Criteria:
# Use 4 states: True + True, True + False, False + True, False + False
# Input example:
# No input is given

# Output example:
# AND
# True + True = True
# ...

# OR
# ...

states = [(True, True), (True, False), (False, True), (False, False)]

print ("AND")
for a, b in states:
    result = a and b #Apply the AND operator
    print(f"{a} + {b} = {result}")
print() #Blank line to separate AND and OR tables

print ("OR")
for a, b in states:
    result = a or b #Apply the OR operator
    print(f"{a} + {b} = {result}") #Print the result in the required format