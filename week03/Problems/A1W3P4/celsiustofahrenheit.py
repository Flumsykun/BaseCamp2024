# Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.

# Criteria:
# The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
# Include appropriate headings on your columns.
# The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the internet .
# Input example:
# No input is given

# Output example:
# °C °F
# 10 50
# 20 68

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32
    return (celsius * 9/5) + 32

# Print the table header
print("°C °F")

# Loop through Celsius values from 0 to 100, in steps of 10
for celsius in range(0, 101, 10):
    # Convert the current Celsius value to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)
    # Print the Celsius and corresponding Fahrenheit values
    print(f"{celsius} {int(fahrenheit)}")
    