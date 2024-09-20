# Consider a valid license plate in The Netherlands (see valid patterns below).
# Write a program that begins by reading a string of characters from the user.
# Then your program should display a message indicating whether the characters are representing a valid license plate.

# Valid patterns:
# XX-99-99
# 99-99-XX
# 99-XX-99
# XX-99-XX
# XX-XX-99
# 99-XX-XX
# 99-XXX-9
# 9-XXX-99
# XX-999-X
# X-999-XX
# XXX-99-X
# 9-XX-999
# Input examples:
# License: A-149-HH
# License: 149-A-HH
# Output examples:
# Valid
# Invalid

#use a regular expression to check if the input matches the valid patterns for a license plate
import re
license_plate = input("License: ")

if re.match(r"^[A-Z]{2}-\d{2}-\d{2}$", license_plate) or re.match(r"^\d{2}-\d{2}-[A-Z]{2}$", license_plate) or re.match(r"^\d{2}-[A-Z]{2}-\d{2}$", license_plate) or re.match(r"^[A-Z]{2}-\d{2}-[A-Z]{2}$", license_plate) or re.match(r"^[A-Z]{2}-[A-Z]{2}-\d{2}$", license_plate) or re.match(r"^\d{2}-[A-Z]{2}-[A-Z]{2}$", license_plate) or re.match(r"^\d{2}-[A-Z]{3}-\d$", license_plate) or re.match(r"^\d-[A-Z]{3}-\d{2}$", license_plate) or re.match(r"^[A-Z]{2}-\d{3}-[A-Z]$", license_plate) or re.match(r"^[A-Z]-\d{3}-[A-Z]{2}$", license_plate) or re.match(r"^[A-Z]{3}-\d{2}-[A-Z]$", license_plate) or re.match(r"^\d-[A-Z]{2}-\d{3}$", license_plate):
    print("Valid")
else:
    print("Invalid")
