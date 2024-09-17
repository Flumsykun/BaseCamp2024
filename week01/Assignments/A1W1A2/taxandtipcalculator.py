# Tip is 15 percent of meal amount (without the tax)
# Assume a local tax rate of 21 percent
# Round all numbers to 3 decimals in the output
# Expected Behaviour: After running your code, it should print the following to the standard output and wait for the user input: Please enter the cost (format 'Cost of the meal: xy.wz'):
# Input example:
# Cost of the meal: 23.60

# Output example:
# Tax: 4.956 , Tip: 3.540 , Total: 32.096
# Tip is 15 percent of meal amount (without the tax)
# Assume a local tax rate of 21 percent
# Round all numbers to 3 decimals in the output

while True:
    try:
        # Prompt the user to enter the cost of the meal
        costOfMeal = (input("Enter cost of the meal (format 'Cost of the meal: xy.wz'): "))
        cost = float(costOfMeal[18:24])
        break  # Exit the loop if a valid number is entered
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Please enter a valid number.")

# Calculate tax and tip
tax = round(cost * 0.21, 3)
tip = round(cost * 0.15, 3)

# Output the tax, tip, and total cost
print(f"Tax: {tax} , Tip: {tip} , Total: {round(cost + tax + tip, 3)}")