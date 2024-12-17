import csv
import json
import os
from datetime import datetime

def report_parked_cars(machine_id, from_date, to_date):
    """
    Generate a report of parked cars for a specific machine within a date range.

    Args:
        machine_id (str): The ID of the parking machine.
        from_date (datetime): The start date for the report.
        to_date (datetime): The end date for the report.

    Outputs:
        A CSV file containing parked cars during the specified period.
    """
    # Define file paths for input (JSON) and output (CSV)
    json_file = f"{machine_id}_state.json"
    output_file = f"parkedcars_{machine_id}.csv"

    # Check if the output file already exists and delete it to avoid write issues
    if os.path.exists(output_file):
        os.remove(output_file)

    # Open CSV file to write the report
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["license_plate", "checked_in", "checked_out", "parking_fee"])

        # Check if the machine's JSON state file exists
        if os.path.exists(json_file):
            with open(json_file, "r") as file:
                cars = json.load(file)
                for car in cars:
                    check_in = datetime.strptime(car["check_in"], "%Y-%m-%d %H:%M:%S")
                    # Include cars parked within the date range
                    if from_date <= check_in <= to_date:
                        check_out = "None"
                        parking_fee = 0.0
                        writer.writerow([car["license_plate"], car["check_in"], check_out, f"{parking_fee:.1f}"])
    print(f"Report generated: {output_file}")

def report_total_fees(from_date, to_date):
    """
    Generate a report of total parking fees collected by all parking machines within a date range.

    Args:
        from_date (datetime): The start date for the report.
        to_date (datetime): The end date for the report.

    Outputs:
        A CSV file containing total fees for each parking machine.
    """
    # Define the output file for the total fees report
    output_file = "total_parking_fees.csv"

    # Check if the output file already exists and delete it to avoid write issues
    if os.path.exists(output_file):
        os.remove(output_file)

    total_fees = {}

    # Iterate through all JSON state files to calculate fees
    for file in os.listdir():
        if file.endswith("_state.json"):
            machine_id = file.split("_")[0]
            total_fees[machine_id] = 0

            with open(file, "r") as f:
                cars = json.load(f)
                for car in cars:
                    check_in = datetime.strptime(car["check_in"], "%Y-%m-%d %H:%M:%S")
                    if from_date <= check_in <= to_date:
                        total_fees[machine_id] += 5.0  # Replace with proper fee calculation

    # Write the total fees to a CSV file
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["car_parking_machine", "total_parking_fee"])
        for machine, fee in total_fees.items():
            writer.writerow([machine, f"{fee:.1f}"])
    print(f"Report generated: {output_file}")

def main():
    """
    Main menu for generating parking reports.
    Users can choose to report parked cars or total collected fees.
    """
    while True:
        # Display the menu options
        print("\n[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print("[Q] Quit program")

        # Get user choice
        choice = input("Choice: ").strip().upper()

        if choice == "P":
            # Get inputs for parked cars report
            machine_id = input("Machine ID: ").strip()
            from_date = datetime.strptime(input("From (DD-MM-YYYY): "), "%d-%m-%Y")
            to_date = datetime.strptime(input("To (DD-MM-YYYY): "), "%d-%m-%Y")
            report_parked_cars(machine_id, from_date, to_date)

        elif choice == "F":
            # Get inputs for total fees report
            from_date = datetime.strptime(input("From (DD-MM-YYYY): "), "%d-%m-%Y")
            to_date = datetime.strptime(input("To (DD-MM-YYYY): "), "%d-%m-%Y")
            report_total_fees(from_date, to_date)

        elif choice == "Q":
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
