import csv
import os
from datetime import datetime


def report_parked_cars(machine_id, from_date, to_date):
    """Report all parked cars for a specific machine."""
    json_file = f"{machine_id}.json"
    if not os.path.exists(json_file):
        print("No data found for this parking machine.")
        return

    # Lees JSON-bestand
    with open(json_file, "r") as file:
        data = json.load(file)

    from_date = datetime.strptime(from_date, "%d-%m-%Y")
    to_date = datetime.strptime(to_date, "%d-%m-%Y")

    with open(f"parkedcars_{machine_id}_from_{from_date}_to_{to_date}.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(["license_plate", "check-in", "check-out", "parking_fee"])
        for car in data:
            check_in = datetime.strptime(car["check_in"], "%Y-%m-%d %H:%M:%S")
            if from_date <= check_in <= to_date:
                writer.writerow([car["license_plate"], car["check_in"], "None", "0"])


def report_total_fees(from_date, to_date):
    """Report total fees for all machines."""
    with open("total_parking_fees.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["car_parking_machine", "total_parking_fee"])
        for machine_file in os.listdir():
            if machine_file.endswith(".json"):
                machine_id = machine_file.split(".")[0]
                # Som alle kosten (simpele placeholder)
                writer.writerow([machine_id, 100.0])


# Menu
def main():
    while True:
        print("[P] Report all parked cars during a parking period")
        print("[F] Report total collected parking fees")
        print("[Q] Quit")
        choice = input("Enter your choice: ").strip().upper()

        if choice == "P":
            machine_id = input("Enter machine ID: ").strip()
            from_date = input("From date (DD-MM-YYYY): ").strip()
            to_date = input("To date (DD-MM-YYYY): ").strip()
            report_parked_cars(machine_id, from_date, to_date)
        elif choice == "F":
            from_date = input("From date (DD-MM-YYYY): ").strip()
            to_date = input("To date (DD-MM-YYYY): ").strip()
            report_total_fees(from_date, to_date)
        elif choice == "Q":
            break


if __name__ == "__main__":
    main()
