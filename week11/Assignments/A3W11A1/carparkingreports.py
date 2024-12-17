import csv
import json
import os
from datetime import datetime


def report_parked_cars(machine_id, from_date, to_date):

        json_file = f"{machine_id}_state.json"
        output_file = f"parkedcars_{machine_id}_from_{from_date.strftime('%d-%m-%Y')}_to_{to_date.strftime('%d-%m-%Y')}.csv"

        # Maak een leeg bestand aan als er geen data is
        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow(["license_plate", "checked_in", "checked_out", "parking_fee"])

            if not os.path.exists(json_file):
                print(f"No data found for machine '{machine_id}'. Empty report generated.")
                return

        with open(json_file, "r") as file:
            data = json.load(file)

        for car in data:
            check_in = datetime.strptime(car["check_in"], "%Y-%m-%d %H:%M:%S")
            if from_date <= check_in <= to_date:
                writer.writerow([car["license_plate"], car["check_in"], "None", "0"])

        print(f"Report saved to {output_file}")



def report_total_fees(from_date, to_date):
    """Report total fees for all machines."""
    with open("total_parking_fees.csv", "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["car_parking_machine", "total_parking_fee"])
        for machine_file in os.listdir():
            if machine_file.endswith(".json"):
                machine_id = machine_file.split(".")[0]
                writer.writerow([machine_id, 100.0])


# Menu
def main():
        while True:
            print("[P] Report all parked cars during a parking period for a specific parking machine")
            print("[F] Report total collected parking fee during a parking period for all parking machines")
            print("[Q] Quit program")
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
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    #report_parked_cars(1, )
    main()
