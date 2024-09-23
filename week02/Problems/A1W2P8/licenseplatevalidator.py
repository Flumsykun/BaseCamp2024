import re

# Define the combined regular expression pattern for all valid license plate formats
pattern = (
    r"^[A-Z]{2}-\d{2}-\d{2}$|"
    r"^\d{2}-\d{2}-[A-Z]{2}$|"
    r"^\d{2}-[A-Z]{2}-\d{2}$|"
    r"^[A-Z]{2}-\d{2}-[A-Z]{2}$|"
    r"^[A-Z]{2}-[A-Z]{2}-\d{2}$|"
    r"^\d{2}-[A-Z]{2}-[A-Z]{2}$|"
    r"^\d{2}-[A-Z]{3}-\d$|"
    r"^\d-[A-Z]{3}-\d{2}$|"
    r"^[A-Z]{2}-\d{3}-[A-Z]$|"
    r"^[A-Z]-\d{3}-[A-Z]{2}$|"
    r"^[A-Z]{3}-\d{2}-[A-Z]$|"
    r"^\d-[A-Z]{2}-\d{3}$"
)

# Read the license plate input from the user
license_plate = input("License: ")

# Check if the input matches the combined pattern
if re.match(pattern, license_plate):
    print("Valid")
else:
    print("Invalid")
