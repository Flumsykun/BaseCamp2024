# make a program that takes out integers from strings
# a1b2c3! >> abc!

# Step 1: Ask the user for input
# Use input, assignments, variables, string,

text = input("Enter a text: ")

# the formatted text is empty first
text_without_digits = ""

# Step 2: Check each character of the string, character by character for a integer
# string, for - loop

for char in text:

    # Step 3: check if the char is not an int
    if not (char.isdigit()):
        # Step 3b: Remember the int
        text_without_digits += char

    # Print the formatted text
    print(text_without_digits)
