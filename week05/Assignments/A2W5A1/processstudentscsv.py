import csv
import re
from datetime import datetime

# Function to validate the student number


def validate_student_number(student_number):
    return bool(re.match(r'^0[89]\d{5}$', student_number))

# Function to validate names (first and last)


def validate_name(name):
    return bool(re.match(r'^[A-Za-z]+$', name))

# Function to validate date of birth (YYYY-MM-DD)


def validate_dob(dob):
    try:
        date_obj = datetime.strptime(dob, '%Y-%m-%d')
        return 1960 <= date_obj.year <= 2004
    except ValueError:
        return False

# Function to validate the study program


def validate_study_program(program):
    return program in ['INF', 'TINF', 'CMD', 'AI']

# Function to validate all data in a row


def validate_data(row):
    student_number, first_name, last_name, dob, study_program = row
    invalid_data = []

    # Validate each field
    if not validate_student_number(student_number):
        invalid_data.append(student_number)
    if not validate_name(first_name):
        invalid_data.append(first_name)
    if not validate_name(last_name):
        invalid_data.append(last_name)
    if not validate_dob(dob):
        invalid_data.append(dob)
    if not validate_study_program(study_program):
        invalid_data.append(study_program)

    return invalid_data

# Function to load CSV data


def load_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip headers
        student_data = [row for row in reader]
    return student_data

# Main processing function


def process_student_data(filename):
    student_data = load_data(filename)
    valid_rows = []
    corrupted_rows = []

    for row in student_data:
        invalid_data = validate_data(row)
        if invalid_data:
            # Add the row and details about invalid fields
            corrupted_rows.append(
                row + ['INVALID DATA: ' + ', '.join(invalid_data)])
        else:
            valid_rows.append(row)

    # Output valid rows
    print("### VALID LINES ###")
    for valid_row in valid_rows:
        print(valid_row)

    # Output corrupted rows with reasons
    print("\n### CORRUPT LINES ###")
    for corrupt_row in corrupted_rows:
        print(corrupt_row)


# Example usage
if __name__ == "__main__":
    process_student_data('students.csv')
