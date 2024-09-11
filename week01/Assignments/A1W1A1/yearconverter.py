# Implement a program that given a number of years as input prints the number of months and days as output.

# Criteria:
# keep the problem simple
# no leap year
# each year is 365 days and 12 months
# Expected Program Behavior: After running the program, the program will wait for the user input.
# The user will enter the full string Years: 5.
# The program can provide a proper message to guide the user about the correct input format.
# The program must slice the input and extract the number to process and produce the result.
# Input example:
# Years: 5

# Output example:
# Months: 60, Days: 1825

# Expected Output: The program will output the number of months and days based on the input years.
def main():
    input_years = input("Enter a number of years in the format 'Years: X': ")

    # Check if the input contains a colon
    if ":" in input_years:
        try:
            number_of_years = input_years.split(":")[1].strip()
            months = int(number_of_years) * 12
            days = int(number_of_years) * 365

            output = f"Months: {months}, Days: {days}"
            print(output)
        except ValueError:
            print("Invalid number format. Please enter a valid number of years.")
    else:
        print("Invalid input format. Please enter the input in the format 'Years: X'.")

if __name__ == "__main__":
    main()