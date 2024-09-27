from datetime import datetime

# Check if first name is valid
def is_name_valid(name: str) -> bool:
    return name.isalpha() and len(name) >= 2 and len(name) <= 10 and name[0].isupper()

# Check if last name is valid
def is_last_name_valid(name: str) -> bool:
    parts = name.split(" ")
    return len(name) >= 2 and len(name) <= 11 and all(part.isalpha() and part[0].isupper() for part in parts)

# Check if job title is valid
def is_title_valid(title: str) -> bool:
    return len(title) >= 10 and all(x.isalpha() or x.isspace() for x in title)

# Check if salary is valid
def validate_salary(salary_input: str) -> bool:
    try:
        salary = salary_input.replace(".", "").replace(",", ".")
        float(salary)
        return True
    except ValueError:
        return False

# Check if date is valid
def validate_date(date_input: str) -> bool:
    try:
        datetime.strptime(date_input, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Main logic for asking user input and generating the letter
def main():
    while True:
        try:
            response = input("More Letters? (Yes or No): ").strip().lower()
            if response == "no":
                break

            letter_type = input("Job Offer or Rejection? ").strip().lower()

            # Job Offer case
            if letter_type == "job offer":
                first_name = input("First Name? ").strip()
                last_name = input("Last Name? ").strip()
                job_title = input("Job Title? ").strip()
                annual_salary = input("Annual Salary? ").strip()
                start_date = input("Start Date? (YYYY-MM-DD) ").strip()

                # Validate inputs
                if not is_name_valid(first_name):
                    print("Input error: Invalid first name.")
                    continue
                if not is_last_name_valid(last_name):
                    print("Input error: Invalid last name.")
                    continue
                if not is_title_valid(job_title):
                    print("Input error: Invalid job title.")
                    continue
                if not validate_salary(annual_salary):
                    print("Input error: Invalid salary.")
                    continue
                if not validate_date(start_date):
                    print("Input error: Invalid date.")
                    continue

                # Print final letter
                print("Here is the final letter to send:")
                print(f"Dear {first_name} {last_name},")
                print(f"After careful evaluation of your application for the position of {job_title},")
                print(f"we are glad to offer you the job. Your salary will be {annual_salary} euro annually.")
                print(f"Your start date will be on {start_date}. Please do not hesitate to contact us with any questions.")
                print("Sincerely,")
                print("HR Department of XYZ")

            # Rejection case
            elif letter_type == "rejection":
                first_name = input("First Name? ").strip()
                last_name = input("Last Name? ").strip()
                job_title = input("Job Title? ").strip()
                feedback_choice = input("Feedback? (Yes or No) ").strip().lower()

                # Validate inputs
                if not is_name_valid(first_name):
                    print("Input error: Invalid first name.")
                    continue
                if not is_last_name_valid(last_name):
                    print("Input error: Invalid last name.")
                    continue
                if not is_title_valid(job_title):
                    print("Input error: Invalid job title.")
                    continue

                # Check feedback
                feedback_statement = ""
                if feedback_choice == "yes":
                    feedback_statement = input("Enter your Feedback (One Statement): ").strip()

                # Print final letter
                print("Here is the final letter to send:")
                print(f"Dear {first_name} {last_name},")
                print(f"After careful evaluation of your application for the position of {job_title},")
                print("at this moment we have decided to proceed with another candidate.")
                if feedback_statement:
                    print("Here we would like to provide you our feedback about the interview.")
                    print(feedback_statement)
                print("We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.")
                print("Sincerely,")
                print("HR Department of XYZ")

            else:
                print("Invalid response. Please choose 'Job Offer' or 'Rejection'.")
        
        except EOFError:
            print("Error: No more input available.")
            break

# Run the main function
if __name__ == "__main__":
    main()
