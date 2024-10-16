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
        year = date_obj.year
        return 1960 <= year <= 2004
    except ValueError:
        return False


# Function to validate the study program
def validate_study_program(program):
    return program in ['INF', 'TINF', 'CMD', 'AI']


# Function to validate all data in a row
def validate_data(student_number, first_name, last_name, dob, study_program):
    invalid_fields = []

    if not validate_student_number(student_number):
        invalid_fields.append(student_number)
    if not validate_name(first_name):
        invalid_fields.append(first_name)
    if not validate_name(last_name):
        invalid_fields.append(last_name)
    if not validate_dob(dob):
        invalid_fields.append(dob)
    if not validate_study_program(study_program):
        invalid_fields.append(study_program)

    return invalid_fields


# Function to process the dataset
def process_dataset(file_path):
    valid_rows = []
    corrupt_rows = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row if present

        for row in reader:
            student_number, first_name, last_name, dob, study_program = row

            # Validate the entire row
            invalid_fields = validate_data(student_number, first_name, last_name, dob, study_program)

            # Categorize the row
            if invalid_fields:
                corrupt_rows.append(f"{','.join(row)} => INVALID DATA: {invalid_fields}")
            else:
                valid_rows.append(','.join(row))

    # Output the results
    print("### VALID LINES ###")
    for valid_row in valid_rows:
        print(valid_row)

    print("\n### CORRUPT LINES ###")
    for corrupt_row in corrupt_rows:
        print(corrupt_row)


# Example usage
process_dataset('students.csv')