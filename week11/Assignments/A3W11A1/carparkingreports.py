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
    output_file = f"parkedcars_{machine_id}_from_{from_date.strftime('%d-%m-%Y')}_to_{to_date.strftime('%d-%m-%Y')}.csv"


    if not os.path.exists(json_file):
        print(f"JSON state file for machine '{machine_id}' not found.")
        return

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["license_plate", "checked_in", "checked_out", "parking_fee"])

        with open(json_file, "r") as file:
            cars = json.load(file)
            for car in cars:
                check_in = datetime.strptime(car["check_in"], "%m-%d-%Y %H:%M:%S")
                check_out = datetime.strptime(car["check_out"], "%m-%d-%Y %H:%M:%S") if car["check_out"] else None

                if from_date <= check_in <= to_date:
                    parking_fee = calculate_fee(check_in, check_out)
                    writer.writerow([car["license_plate"], car["check_in"], car["check_out"] or "None", f"{parking_fee:.1f}"])
    print(f"Report generated: {output_file}")


def calculate_fee(check_in, check_out):
    """
    Calculate the parking fee based on check-in and check-out times.
    Args:
        check_in (datetime): The check-in time.
        check_out (datetime): The check-out time, or None if the car is still parked.
    Returns:
        float: The calculated parking fee.
    """
    if not check_out:
        return 0.0  # No fee for cars that have not checked out
    duration = (check_out - check_in).total_seconds() / 3600  # Duration in hours
    return round(duration * 5.0, 1)  # Assume €5 per hour


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
    output_file = f"totalfee_from_{from_date.strftime('%d-%m-%Y')}_to_{to_date.strftime('%d-%m-%Y')}.csv"

    # Check if the output file already exists and delete it to avoid write issues
    if os.path.exists(output_file):
        os.remove(output_file)

    total_fees = {}

    # Iterate through all JSON state files to calculate fees
    for file in os.listdir():
        if file.endswith("_state.json"):
            machine_id = file.split("_state.json")[0]
            total_fees[machine_id] = 0  # Initialize total fees for the machine

            with open(file, "r") as f:
                cars = json.load(f)
                for car in cars:
                    check_in = datetime.strptime(car["check_in"], "%m-%d-%Y %H:%M:%S")
                    check_out = datetime.strptime(car["check_out"], "%m-%d-%Y %H:%M:%S") if car["check_out"] else None

                    # Only include cars that were checked out within the specified date range
                    if from_date <= check_in <= to_date or (check_out and from_date <= check_out <= to_date):
                        total_fees[machine_id] += calculate_fee(check_in, check_out)

    # Write the total fees to a CSV file
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["car_parking_machine", "total_parking_fee"])
        for machine, fee in total_fees.items():
            writer.writerow([machine, f"{fee:.1f}"])
    print(f"Report generated: {output_file}")

def update_state_file(machine_id, cars):
    """
    Update the JSON state file for a parking machine.
    Args:
        machine_id (str): The ID of the parking machine.
        cars (list): The list of parked cars.
    """
    json_file = f"{machine_id}_state.json"
    with open(json_file, "w") as file:
        json.dump(cars, file, indent=4)


def main():
    """
    Main menu for generating parking reports.
    Users can choose to report parked cars or total collected fees.
    """
    inputs = input("Enter inputs (comma-separated for parameters, one per line): ").strip().splitlines()

    if not inputs:
        print("No input provided.")
        return

    input_index = 0

    while input_index < len(inputs):
        print("\n[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print("[Q] Quit program")

        choice = inputs[input_index].strip().upper()
        input_index += 1

        if choice == "P":
            if input_index >= len(inputs):
                print("Missing parameters for reporting parked cars.")
                break

            params = inputs[input_index].strip().split(",")
            input_index += 1

            if len(params) == 3:
                machine_id, from_date, to_date = params
                from_date = datetime.strptime(from_date.strip(), "%d-%m-%Y")
                to_date = datetime.strptime(to_date.strip(), "%d-%m-%Y")
                report_parked_cars(machine_id.strip(), from_date, to_date)
            else:
                print("Invalid input format for reporting parked cars. Expected: machine_id,from_date,to_date")

        elif choice == "F":
            if input_index >= len(inputs):
                print("Missing parameters for reporting total fees.")
                break

            params = inputs[input_index].strip().split(",")
            input_index += 1

            if len(params) == 2:
                from_date, to_date = params
                from_date = datetime.strptime(from_date.strip(), "%d-%m-%Y")
                to_date = datetime.strptime(to_date.strip(), "%d-%m-%Y")
                report_total_fees(from_date, to_date)
            else:
                print("Invalid input format for reporting total fees. Expected: from_date,to_date")

        elif choice == "Q":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
