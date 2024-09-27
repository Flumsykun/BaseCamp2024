from datetime import datetime


def is_name_valid(name: str) -> bool:
    """Check if first name is valid."""
    return name.isalpha() and 2 <= len(name) <= 10 and name[0].isupper()


def is_last_name_valid(name: str) -> bool:
    """Check if last name is valid."""
    parts = name.split(" ")
    return 2 <= len(name) <= 11 and all(part.isalpha() and part[0].isupper() for part in parts)


def is_title_valid(title: str) -> bool:
    """Check if job title is valid."""
    return len(title) >= 10 and all(x.isalpha() or x.isspace() for x in title)


def is_salary_valid(salary_input: str) -> bool:
    """Check if salary is valid."""
    try:
        salary = salary_input.replace(".", "").replace(",", ".")
        float(salary)
        return True
    except ValueError:
        return False


def is_date_valid(date_input: str) -> bool:
    """Check if date is valid."""
    try:
        datetime.strptime(date_input, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def main():
    """Main logic for asking user input and generating the letter."""
    while True:
        try:
            response = input("More Letters? (Yes or No): ").strip().lower()
            if response == "no":
                break

            letter_type = input("Job Offer or Rejection? ").strip().lower()

            if letter_type == "job offer":
                first_name = input("First Name? ").strip()
                last_name = input("Last Name? ").strip()
                job_title = input("Job Title? ").strip()
                annual_salary = input("Annual Salary? ").strip()
                start_date = input("Start Date? (YYYY-MM-DD) ").strip()

                if not is_name_valid(first_name):
                    print("Input error: Invalid first name.")
                    continue
                if not is_last_name_valid(last_name):
                    print("Input error: Invalid last name.")
                    continue
                if not is_title_valid(job_title):
                    print("Input error: Invalid job title.")
                    continue
                if not is_salary_valid(annual_salary):
                    print("Input error: Invalid salary.")
                    continue
                if not is_date_valid(start_date):
                    print("Input error: Invalid date.")
                    continue

                print("Here is the final letter to send:")
                print(f"Dear {first_name} {last_name},")
                print(
                    f"After careful evaluation of your"
                    f"application for the position of {job_title},"
                )
                print(
                    f"we are glad to offer you the job. "
                    f"Your salary will be {annual_salary} euro annually."
                )
                print(
                    f"Your start date will be on {start_date}. "
                    "Please do not hesitate to contact us with any questions."
                )
                print("Sincerely,")
                print("HR Department of XYZ")

            elif letter_type == "rejection":
                first_name = input("First Name? ").strip()
                last_name = input("Last Name? ").strip()
                job_title = input("Job Title? ").strip()
                feedback_choice = input(
                    "Feedback? (Yes or No) ").strip().lower()

                if not is_name_valid(first_name):
                    print("Input error: Invalid first name.")
                    continue
                if not is_last_name_valid(last_name):
                    print("Input error: Invalid last name.")
                    continue
                if not is_title_valid(job_title):
                    print("Input error: Invalid job title.")
                    continue

                feedback_statement = ""
                if feedback_choice == "yes":
                    feedback_statement = input(
                        "Enter your Feedback (One Statement): ").strip()

                print("Here is the final letter to send:")
                print(f"Dear {first_name} {last_name},")
                print(
                    f"After careful evaluation of "
                    f"your application for the position of {job_title},")
                print("at this moment we have decided "
                      "to proceed with another candidate.")
                if feedback_statement:
                    print("Here we would like to provide"
                          "you our feedback about the interview.")
                    print(feedback_statement)
                print("We wish you the best in finding"
                      "your future desired career."
                      "Please do not hesitate to contact us with any questions.")
                print("Sincerely,")
                print("HR Department of XYZ")

            else:
                print(
                    "Invalid response. Please choose 'Job Offer' or "
                    "'Rejection'.")
        except EOFError:
            print("Error: No more input available.")
            break


if __name__ == "__main__":
    main()
