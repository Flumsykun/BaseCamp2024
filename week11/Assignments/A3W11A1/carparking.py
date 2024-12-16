import json
import math
import os
from datetime import datetime


class CarParkingMachine:
    all_parking_machines = []

    def __init__(self, id, capacity=10, hourly_rate=2.50):
        """Initialize the parking machine."""
        self.machine_id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.json_file = f"{self.machine_id}.json"
        self.parked_cars = {}
        self.load_parked_cars()
        CarParkingMachine.all_parking_machines.append(self)

    def load_parked_cars(self):
        """Load parked cars from JSON file."""
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as file:
                data = json.load(file)
                for car in data:
                    self.parked_cars[car["license_plate"]] = datetime.strptime(car["check_in"], "%Y-%m-%d %H:%M:%S")

    def save_parked_cars(self):
        """Save parked cars to JSON file."""
        data = [{"license_plate": plate, "check_in": time.strftime("%Y-%m-%d %H:%M:%S")} for plate, time in
                self.parked_cars.items()]
        with open(self.json_file, "w") as file:
            json.dump(data, file, indent=4)

    def check_in(self, license_plate, check_in=None):
        """Check if a car can check-in and save state."""

        for machine in CarParkingMachine.all_parking_machines:
            if license_plate in machine.parked_cars:
                return False

        if len(self.parked_cars) >= self.capacity:
            return False  # Vol
        check_in = check_in or datetime.now()
        self.parked_cars[license_plate] = check_in
        self.save_parked_cars()
        return True

    def check_out(self, license_plate):
        """Check out a car, calculate fee, and save state."""
        if license_plate not in self.parked_cars:
            return None
        fee = self.get_parking_fee(license_plate)
        del self.parked_cars[license_plate]
        self.save_parked_cars()
        return fee

    def get_parking_fee(self, license_plate):
        """Calculate the parking fee."""
        if license_plate not in self.parked_cars:
            return None
        check_in_time = self.parked_cars[license_plate]
        duration = datetime.now() - check_in_time
        hours = math.ceil(duration.total_seconds() / 3600)
        return round(min(hours, 24) * self.hourly_rate, 2)


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in

    def __repr__(self):
        return f"<ParkedCar {self.license_plate} at {self.check_in}>"


class CarParkingLogger:
    def __init__(self, machine_id):
        """Initialize the logger with a machine ID."""
        self.machine_id = machine_id
        self.log_file = "carparklog.txt"

    def log_check_in(self, license_plate):
        """Log a car check-in."""
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        log_entry = f"{timestamp};cpm_name={self.machine_id};license_plate={license_plate};action=check-in\n"
        with open(self.log_file, "a") as f:
            f.write(log_entry)

    def log_check_out(self, license_plate, parking_fee):
        """Log a car check-out."""
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        log_entry = f"{timestamp};cpm_name={self.machine_id};license_plate={license_plate};action=check-out;parking_fee={parking_fee}\n"
        with open(self.log_file, "a") as f:
            f.write(log_entry)

    def get_machine_fee_by_day(self, search_date):
        """Calculate the total parking fee for this machine on a specific day."""
        total_fee = 0.0
        search_date = datetime.strptime(search_date, "%d-%m-%Y").date()
        with open(self.log_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(";")
                if len(parts) >= 5:
                    timestamp = datetime.strptime(parts[0], "%d-%m-%Y %H:%M:%S")
                    machine_id = parts[1].split("=")[1]
                    if machine_id.lower() == self.machine_id.lower() and timestamp.date() == search_date:
                        action = parts[3].split("=")[1]
                        if action == "check-out":
                            fee = float(parts[4].split("=")[1])
                            total_fee += fee
        return round(total_fee, 2)

    def get_total_car_fee(self, license_plate):
        """Calculate the total fee for a specific car across all machines."""
        total_fee = 0.0
        with open(self.log_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(";")
                if len(parts) >= 5:
                    plate = parts[2].split("=")[1]
                    if plate == license_plate:
                        action = parts[3].split("=")[1]
                        if action == "check-out":
                            fee = float(parts[4].split("=")[1])
                            total_fee += fee
        return round(total_fee, 2)


def main_menu():
    try:
        machine_id = input("Enter the parking machine ID: ").strip()
        parking_machine = CarParkingMachine(machine_id)

        while True:
            print("\nMenu:")
            print("[I] Check-in car by license plate")
            print("[O] Check-out car by license plate")
            print("[Q] Quit program")
            choice = input("Choose an option: ").strip().upper()

            if choice == "I":
                license_plate = input("License: ").strip()
                if parking_machine.check_in(license_plate):
                    print("License registered")
                else:
                    if len(parking_machine.parked_cars) >= parking_machine.capacity:
                        print("Capacity reached!")
                    else:
                        print("License already checked in!")

            elif choice == "O":
                license_plate = input("License: ").strip()
                fee = parking_machine.check_out(license_plate)
                if fee is None:
                    print(f"License {license_plate} not found!")
                else:
                    print(f"Parking fee: {fee:.2f} EUR")

            elif choice == "Q":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose again.")
    except EOFError:
        print("\nNo input provided. Exiting program.")


if __name__ == "__main__":
    main_menu()
