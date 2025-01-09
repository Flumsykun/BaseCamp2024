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
        self.json_file = f"{self.machine_id}_state.json"
        self.parked_cars = {}  # Stores license_plate -> ParkedCar objects
        self.logger = CarParkingLogger(self.machine_id)  # Add logger instance
        self.load_parked_cars()
        CarParkingMachine.all_parking_machines.append(self)

    def load_parked_cars(self):
        """Load parked cars from JSON file."""
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as file:
                data = json.load(file)
                for car in data:
                    self.parked_cars[car["license_plate"]] = ParkedCar(license_plate=car["license_plate"],
                                                                       check_in=datetime.strptime(car["check_in"],
                                                                                                  "%m-%d-%Y %H:%M:%S"))

    def save_parked_cars(self):
        """Save parked cars to JSON file."""
        data = [{"license_plate": car.license_plate, "check_in": car.check_in.strftime("%m-%d-%Y %H:%M:%S")} for car in
                self.parked_cars.values()]
        with open(self.json_file, "w") as file:
            json.dump(data, file, indent=4)

    def check_in(self, license_plate, check_in=None):
        """Check if a car can check-in and save state."""
        # Check if the car is already parked in any machine
        for machine in CarParkingMachine.all_parking_machines:
            if license_plate in machine.parked_cars:
                return False

        if len(self.parked_cars) >= self.capacity:
            return False  # Capacity reached
        check_in = check_in or datetime.now()
        self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
        self.logger.log_check_in(license_plate)  # Log check-in
        self.save_parked_cars()
        return True

    def check_out(self, license_plate):
        """Check out a car, calculate fee, and save state."""
        if license_plate not in self.parked_cars:
            return None
        parked_car = self.parked_cars.pop(license_plate)
        self.save_parked_cars()
        fee = self.get_parking_fee(parked_car)
        self.logger.log_check_out(license_plate, fee)  # Log check-out
        return fee

    def get_parking_fee(self, parked_car):
        """Calculate the parking fee."""
        duration = datetime.now() - parked_car.check_in
        hours = math.ceil(duration.total_seconds() / 3600)
        return round(min(hours, 24) * self.hourly_rate, 2)


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingLogger:
    def __init__(self, machine_id):
        """Initialize the logger with a machine ID."""
        self.machine_id = machine_id
        self.log_file = "carparklog.txt"

    def log_check_in(self, license_plate):
        """Log a car check-in."""
        timestamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        log_entry = f"{timestamp};cpm_name={self.machine_id};license_plate={license_plate};action=check-in\n"
        with open(self.log_file, "a") as file:
            file.write(log_entry)

    def log_check_out(self, license_plate, parking_fee):
        """Log a car check-out."""
        timestamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        log_entry = f"{timestamp};cpm_name={self.machine_id};license_plate={license_plate};action=check-out;parking_fee={parking_fee}\n"
        with open(self.log_file, "a") as file:
            file.write(log_entry)


def main_menu():
    # machine_id = input("Enter the parking machine ID: ").strip()
    north = "North"
    parking_machine = CarParkingMachine(north)

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


if __name__ == "__main__":
    main_menu()