# Ask the user for the name of item X.
# Then ask the user for the price of item X.
# Finally, ask the user for desired quantity of item X.
# Based on input, calculate how much you have to pay.
# Write the message in the form:
#   "To purchase N units of X you must pay M euros."


# Inputs
name = input("Input the name of item X: ")

price = input("What is the price of", name, "? ")

quantity = input("How many units of", name, "do you want to buy? ")

# Processing
total = price * quantity

# Outputs
print("To purchase", quantity, "units of", name, "you must pay", total, "euros.")