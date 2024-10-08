# Write a program that converts a binary number to decimal.
# Your program should begin by reading the binary number from the user as a string.
# Then it should compute the equivalent decimal number by processing each digit in the binary number.
# Finally, your program should display the equivalent decimal number with an appropriate message.

# Criteria:
# Binary is base 2.
# Decimal is base 10.
# Input example:
# Binary: 1010

# Output example:
# 10

binairy = input("Binary: ")
decimal = 0
for i in range(len(binairy)):
    decimal += int(binairy[i]) * 2 ** (len(binairy) - i - 1)
print(decimal)
