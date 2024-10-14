
import csv
import re
from datetime import datetime

# Function to validate student data


def validate_student_data(student_data):
    valid_rows = []
    corrupted_rows = []

    for row in student_data:
        student_number, first_name, last_name, dob, study_program = row

        invalid_data = []

        # Validate student number
        if not re.match(r'^0[89]\d{6}$', student_number):
            invalid_data.append('Invalid student number')

        # Validate first name and last name
        if not (first_name.isalpha() and last_name.isalpha()):
            invalid_data.append('Invalid name(s)')

        # Validate date of birth
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d')
            if not (1960 <= dob_date.year <= 2004 and 1 <= dob_date.month <= 12 and 1 <= dob_date.day <= 31):
                invalid_data.append('Invalid date of birth')
        except ValueError:
            invalid_data.append('Invalid date of birth format')

        # Validate study program
        if study_program not in ['INF', 'TINF', 'CMD', 'AI']:
            invalid_data.append('Invalid study program')

        # Check for empty values
        if '' in row:
            invalid_data.append('Empty value(s)')

        if invalid_data:
            corrupted_rows.append(
                row + ['INVALID DATA: ' + ', '.join(invalid_data)])
        else:
            valid_rows.append(row)

    return valid_rows, corrupted_rows

# Function to load CSV data


def load_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip headers
        student_data = [row for row in reader]
    return student_data

# Main processing function


def process_student_data(filename):
    student_data = load_data(filename)
    valid_rows, corrupted_rows = validate_student_data(student_data)

    print("### VALID LINES ###")
    for row in valid_rows:
        print(','.join(row))

    print("\n### CORRUPT LINES ###")
    for row in corrupted_rows:
        print(','.join(row))


# Example usage
if __name__ == "__main__":
    process_student_data('students.csv')
