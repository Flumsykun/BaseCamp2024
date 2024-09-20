# Write a program that reads a date from the user and computes its immediate successor.

# Criteria:
# The date will be entered in YYYY-MM-DD format.
# Assume there is no leap year so February always has 28 days.
# The program must employ a function is_input_valid(inp_date) that checks if the provided input satisfies the expected format. The function returns true if the input has correct format. In case of incorrect format, the function must return false.
# The program must print Input format ERROR. Correct Format: YYYY-MM-DD in case the user enters an incorrect input.

# Some examples of incorrect input: 2013/12/30, 2013_12_30, 0213/12/30, 30-12-2013.

# Input examples:
# Input Date: 2013-11-18
# Input Date: 2013-11-30
# Input Date: 2013-12-31
# Output examples:
# Next Date: 2013-11-19
# Next Date: 2013-12-01
# Next Date: 2014-01-01

def is_date_format_valid(date_input):
    """
    Controleert of de invoer voldoet aan het formaat YYYY-MM-DD.
    
    Args:
        date_input (str): De ingevoerde datum als string.
        
    Returns:
        bool: True als de invoer geldig is, anders False.
    """
    # Splits de invoer op de '-' karakters
    date_parts = date_input.split('-')
    
    # Controleer of er precies drie delen zijn
    if len(date_parts) != 3:
        return False
    
    year, month, day = date_parts
    
    # Controleer of de delen alleen cijfers zijn en de juiste lengtes hebben
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    
    return True

def calculate_next_date(current_date):
    """
    Bereken de volgende datum op basis van de ingevoerde datum.
    
    Args:
        current_date (str): De huidige datum in het formaat YYYY-MM-DD.
        
    Returns:
        str: De volgende datum in het formaat YYYY-MM-DD.
    """
    # Splits de datum in jaar, maand en dag en zet ze om naar integers
    year, month, day = map(int, current_date.split('-'))
    
    # Aantal dagen per maand (zonder schrikkeljaren)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verhoog de dag met 1
    day += 1
    
    # Controleer of de dag de limiet van de maand overschrijdt
    if day > days_in_month[month]:
        day = 1
        month += 1
        # Controleer of de maand de limiet van 12 overschrijdt
        if month > 12:
            month = 1
            year += 1
    
    # Format de datum als YYYY-MM-DD
    return f"{year:04d}-{month:02d}-{day:02d}"

# Vraag de gebruiker om een datum
input_date = input("Input Date: ")

# Controleer of de ingevoerde datum geldig is
if is_date_format_valid(input_date):
    next_date = calculate_next_date(input_date)
    print(f"Next Date: {next_date}")
else:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
